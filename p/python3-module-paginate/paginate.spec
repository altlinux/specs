%define _unpackaged_files_terminate_build 1

%define oname paginate

Name: python3-module-%oname
Version: 0.5.6
Release: alt4

Summary: Divides large result sets into pages for easier browsing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/paginate/

# https://github.com/Pylons/paginate.git
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.md CHANGELOG.txt
%python3_sitelibdir/*


%changelog
* Fri Mar 24 2023 Anton Vyatkin <toni@altlinux.org> 0.5.6-alt4
- Fix BuildRequires.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.6-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.6-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140824.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140824
- Initial build for Sisyphus

