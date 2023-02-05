# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=normal

%def_with python
%def_with python3
%def_with ruby
%def_without doc

Name: xapian-bindings
Version: 1.4.22
Release: alt1
Summary: Xapian search engine bindings
License: GPL-2.0-or-later
Group: Development/Databases
Url: http://www.xapian.org/
Vcs: git://git.xapian.org/xapian

Source: http://www.oligarchy.co.uk/xapian/%version/%name-%version.tar
Source100: xapian-bindings.watch
Patch1: xapian-bindings-1.4.15-alt-no-docs.patch

BuildRequires: gcc-c++
BuildRequires: libruby-devel
BuildRequires: libxapian-devel = %version
%if_with ruby
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-ruby
%endif
%if_with python
%setup_python_module %name
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
%endif
%if_with doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-devel
%endif

%description
Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications.
It has built-in support for several families of weighting models
and also supports a rich set of boolean query operators.

This package contains programming language bindings.

%package -n python-module-xapian
Summary: Python bindings for Xapian search engine
Group: Development/Python

%description -n python-module-xapian
Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications.
It has built-in support for several families of weighting models
and also supports a rich set of boolean query operators.

This package provides the files needed for developing Python scripts
which use Xapian.

%package -n python3-module-xapian
Summary: Python 3 bindings for Xapian search engine
Group: Development/Python3

%description -n python3-module-xapian
Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications.
It has built-in support for several families of weighting models
and also supports a rich set of boolean query operators.

This package provides the files needed for developing Python 3 scripts
which use Xapian.

%package -n ruby-xapian
Summary: Ruby bindings for Xapian search engine
Group: Development/Ruby

%description -n ruby-xapian
Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications.
It has built-in support for several families of weighting models
and also supports a rich set of boolean query operators.

This package provides the files needed for developing Ruby scripts
which use Xapian.

%prep
%setup
%if_without doc
%patch1 -p2
%endif
# Link to the libruby for a proper dependency.
sed -i '/_xapian_la_LDFLAGS/s/$/ -lruby/' ruby/Makefile.am

# Workaround to https://bugzilla.altlinux.org/44173
%define ruby_vendorarchdir %(ruby -rrubygems -rrbconfig -e 'puts RbConfig::CONFIG["vendorarchdir"]')

%build
%ifarch %e2k
# http://stackoverflow.com/questions/14892101/
%add_optflags -ftls-model=global-dynamic
%endif
%autoreconf
export RUBY_LIB=%ruby_vendorlibdir
export RUBY_LIB_ARCH=%ruby_vendorarchdir
%configure %{subst_with python} %{subst_with python3} %{subst_with ruby}
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name/

%check
%if_with ruby
  ruby -Iruby -Iruby/.libs -rxapian -e '(p Xapian.version_string) == "%version"'
  make -C ruby check
%endif
%if_with python
  make -C python check
%endif
%if_with python3
  make -C python3 check
%endif

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
%ruby_vendorarchdir/_xapian.so
%ruby_vendorlibdir/xapian.rb
%endif

%changelog
* Sun Feb 05 2023 Vitaly Chikunov <vt@altlinux.org> 1.4.22-alt1
- Update to 1.4.22 (2023-02-02).

* Sun Oct 23 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.21-alt1
- Update to 1.4.21 (2022-09-22).

* Mon Sep 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.15-alt5
- Rebuild with newer libruby(2->3).
- Remove checkinstall test and replace it with tests run in %%check, so that
  ALT beekeeper will try them too.

* Tue Mar 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.15-alt4
- spec: Build ruby module in vendor directories.
- spec: Build ruby-xapian-checkinstall with a simple test.
- spec: Link xapian.so with the libruby to cause proper dependence.

* Tue Jan 11 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.15-alt3
- Fixed build of ruby module.

* Sat Oct 17 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.15-alt2
- fix build

* Mon Mar 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.15-alt1
- new version 1.4.15 (with rpmrb script)

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.5-alt4
- Fix packaging of ruby module.

* Tue Mar 05 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.5-alt3
- Enable building of ruby module

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.5-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-python-obsolete-buildreq-python-dev for xapian-bindings

* Sun Jul 01 2018 Michael Shigorin <mike@altlinux.org> 1.4.5-alt2
- support e2kv4 through %%e2k macro (grenka@)
- merged my changes back
- changed docs knob to doc (see also http://altlinux.org/bootstrap)
- minor spec cleanup: package descriptions need no conditionals

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to latest stable upstream version 1.4.5.
- Enabled building bindings for python-3.

* Tue Oct 17 2017 Michael Shigorin <mike@altlinux.org> 1.4.5-alt0
- new version (watch file uupdate)

* Tue May 09 2017 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- new version (watch file uupdate)

* Fri Jan 27 2017 Michael Shigorin <mike@altlinux.org> 1.4.3-alt1
- new version (watch file uupdate)

* Wed Dec 28 2016 Michael Shigorin <mike@altlinux.org> 1.4.2-alt2
- BOOTSTRAP: introduce doc knob for cyclic BR:
  python-module-sphinx <-> python-module-xapian

* Tue Dec 27 2016 Michael Shigorin <mike@altlinux.org> 1.4.2-alt1
- new version (watch file uupdate)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- new version (watch file uupdate)
- disable sphinx for bootstrap

* Tue Sep 27 2016 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- new version (watch file uupdate)

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
