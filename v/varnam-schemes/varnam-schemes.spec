%define varnamschemesdir %_datadir/varnam/schemes

Name: varnam-schemes
Version: 1.8.0
Release: alt1

Summary: Varnam Language support files
License: MPL-2.0
Group: Graphical desktop/Other
Url: https://varnamproject.com
Vcs: https://github.com/varnamproject/schemes.git

Source: %name-%version.tar

Patch: fix-varnam-schemes-1.8.0-ALT-ruby.patch

BuildRequires: python3 python3-modules-sqlite3
BuildRequires: ruby gem-ffi
BuildRequires: libgovarnam-devel

BuildArch: noarch

%description
%summary.

%prep
%setup
%patch

%build
./build_all_schemes.sh

%install
mkdir -p %buildroot%varnamschemesdir
for s in as bn gu hi kn ml ml-inscript mr ne or pa sa ta te; do
	install schemes/$s/$s.vst %buildroot%varnamschemesdir ;
done

%files
%dir %varnamschemesdir
%varnamschemesdir/*.vst

%changelog
* Mon Apr 14 2025 Ulysses Apokin <ulysses@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus.
