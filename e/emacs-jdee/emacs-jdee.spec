# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-jdee.spec,v 1.8 2006/05/03 12:51:02 eugene Exp $

Version: 2.4.0.1
# %define subver beta6
Release: alt2
Name: emacs-jdee
License: GPL
Group: Editors
Url: http://jdee.sourceforge.net/
Summary: Java Development Environment for Emacs
Summary(ru_RU.UTF-8): Среда разработки Java для Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Requires: emacs-common emacs-cedet emacs-elib 

Source: jdee-%version.tar.gz
Source1: jde-emacs.el

Patch: jdee-2.4.0.1-java.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 18 2002
BuildRequires: emacs-common emacs-base emacs-elib emacs-cedet emacs-devel emacs-leim

BuildRequires: ant ant-contrib

%description
The Java Development Environment for GNU Emacs is a software package that interfaces
Emacs to command-line Java development tools. JDEE features include:
    * JDEE menu with compile, run, debug, build, browse, project, and help commands
    * syntax coloring
    * auto indentation
    * compile error to source links
    * source-level debugging
    * source code browsing
    * make file support
    * automatic code generation
    * Java source interpreter

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%setup -q -n jde
%patch -p1

%build
export CLASSPATH=/usr/share/java/ant-contrib.jar
CEDETDIR=%_emacslispdir/cedet
[ -d $CEDETDIR ] || CEDETDIR=$(sh -c echo /usr/share/emacs/*/lisp/cedet)
ant -Delib.dir=%_emacslispdir/elib -Dcedet.dir=$CEDETDIR


%install
mkdir -p %buildroot%_emacslispdir/jde/java/classes

install -m 644 build/lisp/*.el* %buildroot%_emacslispdir/jde
cp -R java/bsh-commands java/lib %buildroot%_emacslispdir/jde/java
touch %buildroot%_emacslispdir/jde/java/.nosearch

mkdir -p %buildroot%_bindir
install -m 755 lisp/jtags %buildroot%_bindir

mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/23jde.el

%files
%doc doc
%dir %_emacslispdir/jde/
%_emacslispdir/jde/*.elc
%dir %_emacslispdir/jde/java/
%_emacslispdir/jde/java/*
%_emacslispdir/jde/java/.nosearch
%_bindir/*
%config(noreplace) %_emacs_sitestart_dir/23jde.el

%files el
%_emacslispdir/jde/*.el

%changelog
* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.0.1-alt2
- fixed build

* Fri Sep 17 2010 Igor Vlasenko <viy@altlinux.ru> 2.4.0.1-alt1
- New version

* Wed May 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.3.5.1-alt1
- New version, bugfix release
- Fixed build
- Removed incomplete russian translation of package description

* Mon Nov 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.3.5-alt2
- Removed load-path modification
- Added %_emacslispdir/jde/java/.nosearch
- Build with emacs-devel
- Cleanup spec

* Sat Sep 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.3.5-alt1
- New version
- doc and java dirs now belongs to package
- Fixed summary typo (#7859)

* Tue Nov 02 2004 Ivan Fedorov <ns@altlinux.ru> 2.3.4-alt2.beta6
- New beta version

* Wed May 12 2004 Ott Alex <ott@altlinux.ru> 2.3.4-alt2.beta3
- New beta version

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 2.3.4-alt2.beta2
- Move add-on modules to separate package

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 2.3.4-alt1.beta2
- New beta

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 2.3.3-alt6
- Fix dependences

* Wed Dec 10 2003 Ott Alex <ott@altlinux.ru> 2.3.3-alt5
- Release

* Sun Nov 09 2003 Ott Alex <ott@altlinux.ru> 2.3.3-alt4beta6
- Rebuild with cedet

* Mon Sep 29 2003 Ott Alex <ott@altlinux.ru> 2.3.3-alt3beta6
- New beta

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 2.3.3-alt2beta5
- Fixing spec

* Thu Jul 17 2003 Ott Alex <ott@altlinux.ru> 2.3.3-alt1beta5
- New release

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 2.3.2-alt4
- Fixing startup file

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 2.3.2-alt3
- Fixing spec file

* Fri Jan 17 2003 Ott Alex <ott@altlinux.ru> 2.3.2-alt2
- Fixing spec-file

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 2.3.2-alt1
- New Release. Bugfixes

* Tue Dec 24 2002 Ott Alex <ott@altlinux.ru> 2.3.1-alt0.12
- Added optional packages

* Tue Dec 10 2002 Ott Alex <ott@altlinux.ru> 2.3.1-alt0.11
- New Release. Bugfixes

* Wed Dec 04 2002 Ott Alex <ott@altlinux.ru> 2.3.0-alt0.10
- New Release. Many bugfixes

* Tue Nov 12 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.9
- New Release. Many new features and bugfixes

* Mon Sep 23 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.8.beta12
- fixing ant runner

* Wed Sep 11 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.7.beta12
- New beta version

* Thu Sep 05 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.6.beta10
- Fixing spec file and patching source

* Thu Aug 22 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.5.beta10
- Splitting on byte-compiled & source packages

* Wed Aug 14 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.4.beta10
- Patch for using new version of eieio

* Mon Aug 12 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.3.beta10
- Correct BuildRequires & Requires

* Tue Aug 06 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.2.beta10
- Adding right Requires to spec

* Thu Jul 18 2002 Ott Alex <ott@altlinux.ru> 2.2.9-alt0.1.beta10
- Initial build

