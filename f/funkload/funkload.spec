Name: funkload
Version: 1.16.1
Release: alt1

Summary: FunkLoad is a functional and load web tester
License: GPLv2
Group: Development/Other

URL: http://funkload.nuxeo.org/
Source: http://funkload.nuxeo.org/snapshots/funkload-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2010
BuildRequires: python-devel python-module-setuptools

Requires: gnuplot

%description
FunkLoad is a functional and load web tester, written in Python, whose main use cases are:

 * Functional testing of web projects, and thus regression testing as well.
 * Performance testing: by loading the web application and monitoring your servers it helps you to pinpoint bottlenecks.
 * Load testing tool to expose bugs that do not surface in cursory testing, like volume testing or longevity testing.
 * Stress testing tool to overwhelm the web application resources and test the application recoverability.
 * Writing web agents by scripting any web repetitive task, like checking if a site is alive.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/funkload*

%changelog
* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.13.0-alt1.1
- Rebuild with Python-2.7

* Fri Aug 20 2010 Victor Forsiuk <force@altlinux.org> 1.13.0-alt1
- 1.13.0

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 1.11.0-alt1
- Initial build.
