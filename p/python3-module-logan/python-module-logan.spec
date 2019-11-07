%define  modulename logan

Name:    python3-module-%modulename
Version: 0.7.2
Release: alt2

Summary: Logan is a toolkit for building standalone Django applications
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/dcramer/logan

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Source:  %modulename-%version.tar


%description
Logan is a toolkit for running standalone Django applications. It
provides you with tools to create a CLI runner, manage settings, and the
ability to bootstrap the process.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/tests/%modulename/

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt2
- python2 -> python3

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus
