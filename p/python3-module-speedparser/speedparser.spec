%define _unpackaged_files_terminate_build 1
%define oname speedparser

%def_without check

Name: python3-module-%oname
Version: 0.2.0
Release: alt3.git20140816.qa1

Summary: feedparser but faster and worse
License: MIT
Group: Development/Python3
Url: https://github.com/jmoiron/speedparser

BuildArch: noarch

# https://github.com/jmoiron/speedparser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-tools
%if_with check
BuildRequires: python3-module-chardet
BuildRequires: python3-module-lxml
%endif

%description
Speedparser is a black-box "style" reimplementation of the Universal
Feed Parser. It uses some feedparser code for date and authors, but
mostly re-implements its data normalization algorithms based on
feedparser output. It uses lxml for feed parsing and for optional HTML
cleaning. Its compatibility with feedparser is very good for a strict
subset of fields, but poor for fields outside that subset.
See tests/speedparsertests.py for more information on which fields are
more or less compatible and which are not.

%prep
%setup
tar -xf tests/feeds.tar.bz2

find ./ -type f -name '*.py' -exec 2to3-%_python3_version -w -n '{}' +

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3.git20140816.qa1
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2.git20140816.qa1
- NMU: applied repocop patch

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2.git20140816
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140816.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140816.1
- NMU: Use buildreq for BR.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140816
- Initial build for Sisyphus

