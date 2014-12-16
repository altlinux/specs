%define oname icdiff


Summary:        Improved Colored Difference Tool
Name:           %oname
Version:        1.7.1
Release:        alt1
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
mkdir -p %buildroot%_sbindir
install -p -m755 %oname %buildroot%_sbindir/%oname
install -p -m755 git-%oname %buildroot%_sbindir/git-%oname

%files
%doc README.md ChangeLog
%_sbindir/%oname
%_sbindir/git-%oname

%changelog
* Tue Dec 16 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.1-alt1
- Initial build for ALT

