Name: simple-xinit
Version: 0.2
Release: alt1

Summary: launches an X server

License: GPL-2.0
Group: System/X11
URL: https://packages.altlinux.org/sisyphus/srpms/simple-xinit

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-macros-muon
BuildRequires: muon
BuildRequires: gcc

%description
This 200-line C program has two simple jobs. Firstly, it starts an X server
with the specified command line arguments and uses the "-displayfd" option to
let it pick an available value for DISPLAY. Then, it sets up an X client (or a
wrapper to eventually launch one) and its environment. %name has zero implicit
behaviour; all command line parameters and command names are up to the caller.

Synopsis:
  simple-xinit "$client" "$client_args[@]" -- X "$server_args[@]"

%prep
%setup

%build
%muon_meson
%muon_build

%install
%muon_install
# portier is neither public nor OK quality yet.
mv %buildroot%_bindir/{portier,simple}-xinit

%files
%_bindir/simple-xinit

%check
# No tests provided yet.
exit 0

%changelog
* Fri Jun 28 2024 Arseny Maslennikov <arseny@altlinux.org> 0.2-alt1
- Initial build for ALT Sisyphus.
