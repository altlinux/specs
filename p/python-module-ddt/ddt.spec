%define _unpackaged_files_terminate_build 1

%global oname ddt
%def_with check

Name: python-module-ddt
Version: 1.4.2
Release: alt1
Summary: A Python library to multiply test cases
Group: Development/Python
License: MIT
Url: https://pypi.org/project/ddt/

# https://github.com/datadriventests/ddt.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(enum34)

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(yaml)
%endif

%description
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.

%package -n python3-module-%oname
Summary: Data-Driven/Decorated Tests
Group: Development/Python

%description -n python3-module-%oname
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.

%prep
%setup
%autopatch -p1

rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.md
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*

%changelog
* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.1.1 -> 1.4.2.

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- Initial build for ALT (based on CentOS 1.0.1-2.el7.src)
