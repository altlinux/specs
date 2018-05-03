%def_with python
%def_with python3
%def_without ruby
%def_without docs

Name: xapian-bindings
Version: 1.4.5
Release: alt1.1

Summary: Xapian search engine bindings
License: GPL
Group: Development/Other

Url: http://www.xapian.org/
Source: http://www.oligarchy.co.uk/xapian/%version/%name-%version.tar.xz
Source100: xapian-bindings.watch

Patch1: %name-%version-alt-no-docs.patch

%setup_python_module %name

# Automatically added by buildreq on Thu Dec 05 2013
# optimized out: elfutils gnu-config libncurses-devel libstdc++-devel libtinfo-devel pam0_userpass python-base python-modules python-modules-compiler ruby ruby-stdlibs xz
BuildRequires: gcc-c++ libruby-devel libxapian-devel python-dev
%if_with docs
BuildRequires: python-module-sphinx-devel python-module-sphinx
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
%if_with docs
BuildRequires: python3-module-sphinx-devel python3-module-sphinx
%endif
%endif

%{?_with_python:BuildRequires: python-devel}
%{?_with_ruby:BuildRequires: libruby-devel}

BuildRequires: libxapian-devel = %version

%description
Xapian is an Open Source Probabilistic Information Retrieval framework.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package contains programming language bindings.

%if_with python
%package -n python-module-xapian
Summary: Python bindings for Xapian search engine
License: GPL
Group: Development/Python
# force rebuild with libxapian
Requires: libxapian = %version

%description -n python-module-xapian
Xapian is an Open Source Probabilistic Information Retrieval framework.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the files needed for developing Python scripts
which use Xapian.
%endif

%if_with python3
%package -n python3-module-xapian
Summary: Python 3 bindings for Xapian search engine
License: GPL
Group: Development/Python3
# force rebuild with libxapian
Requires: libxapian = %version

%description -n python3-module-xapian
Xapian is an Open Source Probabilistic Information Retrieval framework.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the files needed for developing Python 3 scripts
which use Xapian.
%endif

%if_with ruby
%package -n ruby-xapian
Summary: Ruby bindings for Xapian search engine
License: GPL
Group: Development/Ruby
Requires: libxapian = %version

%description -n ruby-xapian
Xapian is an Open Source Probabilistic Information Retrieval framework.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the files needed for developing Ruby scripts
which use Xapian.
%endif

%prep
%setup
%if_without docs
%patch1 -p2
%endif

%build
%ifarch e2k
# http://stackoverflow.com/questions/14892101/
%add_optflags -ftls-model=global-dynamic
%endif
%if_without docs
%autoreconf
%endif
%configure %{subst_with python} %{subst_with python3} %{subst_with ruby}
%make_build
# FIXME: maybe we should drop %version there as well and get rid of this

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name/

%if_with python
%files -n python-module-xapian
%doc README python/docs/*
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-xapian
%doc README python/docs/*
%python3_sitelibdir/*
%endif

%if_with ruby
%files -n ruby-xapian
%doc README ruby/docs/*
%ruby_sitearchdir/_xapian.so
%ruby_sitelibdir/xapian.rb
%endif

# TODO:
# - package other bindings (perl, tcl...)
# - package docs/examples properly

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to latest stable upstream version 1.4.5.
- Enabled building bindings for python-3.

* Tue Sep 27 2016 Michael Shigorin <mike@altlinux.org> 1.2.23-alt2
- rebuilt against ruby-2.3.1

* Wed Mar 30 2016 Michael Shigorin <mike@altlinux.org> 1.2.23-alt1
- new version (watch file uupdate)

* Fri Jan 01 2016 Michael Shigorin <mike@altlinux.org> 1.2.22-alt1
- new version (watch file uupdate)

* Thu May 21 2015 Michael Shigorin <mike@altlinux.org> 1.2.21-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 1.2.20-alt1
- new version (watch file uupdate)

* Tue Oct 21 2014 Michael Shigorin <mike@altlinux.org> 1.2.19-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 1.2.18-alt1
- new version (watch file uupdate)

* Fri Mar 21 2014 Michael Shigorin <mike@altlinux.org> 1.2.17-alt1
- new version (watch file uupdate)

* Thu Mar 20 2014 Led <led@altlinux.ru> 1.2.16-alt1.1
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 05 2013 Michael Shigorin <mike@altlinux.org> 1.2.16-alt1
- 1.2.16
- merged standalone python-module-xapian and ruby-xapian packages
  which used to build parts of xapian-bindings independently
- dropped libtool related hacks (thanks upstream notice)
- buildreq

* Sat Mar 23 2013 Michael Shigorin <mike@altlinux.org> 1.2.14-alt1
- 1.2.14

* Thu Feb 21 2013 Michael Shigorin <mike@altlinux.org> 1.2.13-alt1
- 1.2.13

* Thu Jun 28 2012 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- 1.2.12

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- 1.2.10
- added watch file
- minor spec cleanup

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt2
- argh, forgotten rebuild

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- 1.2.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt1.1
- Rebuild with Python-2.7

* Tue Aug 16 2011 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 1.2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.2
- Rebuilt for debuginfo

* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1.1
- simplify dependency invariant

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Wed Jun 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt1
- new version 1.0.21 (with rpmrb script)

* Tue May 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.20-alt1
- new version 1.0.20 (with rpmrb script)

* Mon Apr 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt1
- new version 1.0.19 (with rpmrb script)

* Mon Apr 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt1
- new version 1.0.18 (with rpmrb script)

* Sat Feb 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt1
- new version 1.0.17 (with rpmrb script) (fix alt bug #22673)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.1
- Rebuilt with python 2.6

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus
