%define  modulename meinheld

Name:    python-module-%modulename
Version: 0.6.1
Release: alt1

Summary: meinheld is a high performance asynchronous WSGI Web Server (based on picoev)
License: NOASSERTION
Group:   Development/Python
URL:     https://github.com/mopemope/meinheld

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Dec 13 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
