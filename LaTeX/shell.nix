{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages(p: with p; [
      # If python packages need to be included:
      # p.pkgs-name
    ]))
    pkgs.pandoc
    pkgs.which
    pkgs.texliveFull
  ];
  # This fixes the \today command in LaTeX to the current date
  shellHook = ''
    export SOURCE_DATE_EPOCH=$(${pkgs.coreutils}/bin/date +%s)
  '';
}
