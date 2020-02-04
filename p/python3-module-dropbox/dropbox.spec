%define oname dropbox

Name: python3-module-%oname
Version: 9.4.0
Release: alt1

Summary: A Python SDK for integrating with the Dropbox API v2.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dropbox/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner


%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir
%endif

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname/*.py
%python3_sitelibdir/%oname/*.crt
%python3_sitelibdir/%oname/__pycache__/*.pyc
%python3_sitelibdir/%oname-%version-py3.7.egg-info/*


%changelog
* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 9.4.0-alt1
- Initial build.

