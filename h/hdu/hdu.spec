Name:       hdu
Version:    0.2.3.9
Release:    alt2

Summary:    Human-friendly summary of disk usage
License:    GPLv3+
Group:      File tools
Url:        https://bitbucket.org/norok2/hdu
Packager:   Evgenii Terechkov <evg@altlinux.org>

BuildArch:  noarch

Source:     %name-%version.tar
Patch:      %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm


%description
Human-friendly summary of disk usage.

%prep
%setup

%build
subst 's/version=None/version="%version"/' setup.py
%python3_build

%install
%python3_install

%files
%doc README
%_bindir/%name
%python3_sitelibdir/%{name}*


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.3.9-alt2
- Porting on Python3.

* Sat Feb 13 2016 Terechkov Evgenii <evg@altlinux.org> 0.2.3.9-alt1
- 0.2.3.9

* Wed Feb 10 2016 Terechkov Evgenii <evg@altlinux.org> 0.2.2.5-alt1
- Initial build for ALT Linux Sisyphus
