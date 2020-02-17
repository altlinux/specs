%define _unpackaged_files_terminate_build 1

%define oname tmdb3

Name: python3-module-%oname
Version: 0.7.2
Release: alt2

Summary: TheMovieDB.org APIv3 interface
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tmdb3/

BuildArch: noarch

# https://github.com/wagnerrp/pytmdb3.git
Source0: https://pypi.python.org/packages/ec/67/b248c8c4867876c7620d724e7f85f6cf86102d730813891e41b05cc744bd/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-pytest
BuildRequires: python-tools-2to3


%description
This Python module implements the v3 API for TheMovieDb.org, allowing
access to movie and cast information, as well as related artwork.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
nosetests3

%files
%doc LICENSE PKG-INFO README.md
%python3_sitelibdir/*


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt2
- Build for python2 disabled.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20140128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20140128.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140128
- Initial build for Sisyphus

