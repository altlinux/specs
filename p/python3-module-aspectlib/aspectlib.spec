%define _unpackaged_files_terminate_build 1

%define oname aspectlib

Name: python3-module-%oname
Version: 1.4.2
Release: alt3

Summary: An aspect-oriented programming, monkey-patch and decorators library
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/aspectlib/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools


%description
An aspect-oriented programming, monkey-patch and decorators library.
It is useful when changing behavior in existing code is desired.
It includes tools for debugging and testing: simple mock/record and a complete capture/replay framework.

%prep
%setup
# false dependency
grep -qsF "'fields'" setup.py || exit 1
sed -i "/'fields'/d" setup.py

rm -f ./src/%{oname}/py2*.py

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc LICENSE *.rst
%python3_sitelibdir/*


%changelog
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.2-alt3
- Build for python2 disabled.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.2-alt2
- Removed false dependency on `fields`.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
