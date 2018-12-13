%define  modulename meinheld

Name:    python3-module-%modulename
Version: 0.6.1
Release: alt1

Summary: meinheld is a high performance asynchronous WSGI Web Server (based on picoev)
License: NOASSERTION
Group:   Development/Python3
URL:     https://github.com/mopemope/meinheld

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 13 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
