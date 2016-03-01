%define oname icdiff


Summary:        Improved Colored Difference Tool
Name:           %oname
Version:        1.7.3
Release:        alt2
URL:            http://www.jefftk.com/icdiff
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:        PSF
Group: 		File tools

BuildRequires:  python-devel
BuildArch:      noarch
Source0:        %name-%version.tar

%description
Show differences between two files in a two column colored view.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_bindir
install -p -m755 %oname %buildroot%_bindir/%oname
install -p -m755 git-%oname %buildroot%_bindir/git-%oname

%files
%doc README.md ChangeLog
%_bindir/%oname
%_bindir/git-%oname

%changelog
* Tue Mar 01 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt2
- Moved from binaries from %_sbindir to %_bindir (ALT #31848)

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt1
- New version

* Tue Dec 16 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.1-alt1
- Initial build for ALT

