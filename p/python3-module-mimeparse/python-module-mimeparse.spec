%define _unpackaged_files_terminate_build 1

%define oname mimeparse

Name: python3-module-%oname
Version: 1.6.0
Release: alt4

Summary: Basic functions for handling mime-types in python
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/python-mimeparse

# https://github.com/dbtsai/python-mimeparse.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(json)


%description
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of 
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards
      and a 'q' quality parameter.
    - quality():           Determines the quality ('q') of a mime-type
      when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second
      parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality
      ('q') from a list of candidates.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 mimeparse_test.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt4
- Build for python2 disabled.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2.qa1
- NMU: remove %ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1.qa1%ubt
- NMU: applied repocop patch

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1%ubt
- Updated to upstream version 1.6.0.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1.1.1
- (AUTO) subst_x86_64.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.svn20130102.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.svn20130102
- Version 0.1.4
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt1
- build for ALT
