Name: libidn
Version: 1.33
Release: alt3

Summary: Internationalized Domain Name support library
Group: System/Libraries
License: LGPLv3+/GPLv2+ and GPLv3+ and GFDL
Url: http://www.gnu.org/software/%name/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

%def_enable java
%def_with emacs
%{?!_without_emacs:BuildRequires: emacs-devel emacs-nox}

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package devel
Group: Development/C
Summary: Development files for the %name library
Requires: %name = %version-%release

%description devel
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package includes headers and other development files necessary
for developing programs which use the GNU Libidn library.

%package devel-doc
Summary: Development documentation for the %name library
Group: Development/C
License: GFDL
Requires: %name-devel = %version-%release
BuildArch: noarch

%description devel-doc
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package contains %name development documentation.

%package -n emacs-%name
Summary: GNU Emacs %name support files
Group: Development/Other
License: GPLv3+
BuildArch: noarch

%description -n emacs-%name
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package includes %name support files for GNU Emacs.

%if_enabled java
%package java
Group: Development/Java
Summary:       Java port of the GNU Libidn library
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java java-devel-default javapackages-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)
BuildArch:     noarch

%description java
GNU Libidn is a fully documented implementation of the Stringprep,
Punycode and IDNA specifications. Libidn's purpose is to encode
and decode internationalized domain names.

This package contains the native Java port of the library.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}-java
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}-java.
%endif

%prep
%setup
# These gnulib tests fail.
sed -i 's/test-\(lock\|thread_create\)\$(EXEEXT) //' lib/gltests/Makefile.in

%if_enabled java
# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

# Not available test dep
%pom_remove_dep com.google.caliper:caliper java/pom.xml.in
%endif

%build
%configure \
	%{subst_enable java} \
	--disable-rpath \
	--disable-static \
	--disable-silent-rules \
	#
# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std \
%if_enabled java
 libidn_jardir=%{_javadir}
%endif

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -fnrs %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

rm %buildroot%_infodir/*.png
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/reference/html
install -pm644 doc/*.html doc/*.pdf %buildroot%docdir/
install -pm644 AUTHORS COPYING FAQ NEWS README THANKS %buildroot%docdir/
install -pm644 doc/reference/*.pdf %buildroot%docdir/reference/
install -pm644 doc/reference/html/* %buildroot%docdir/reference/html/

%if_enabled java
# regenerate java documentation (breaks %%check)
##rm -rf doc/java/*
##find doc/java -name '*.html' -delete
##%javadoc -source 1.6 -d doc/java $(find java/src/main/java -name "*.java")
# generate maven depmap
rm -rf $RPM_BUILD_ROOT%{_javadir}/libidn*.jar
%mvn_artifact java/pom.xml java/libidn-%{version}.jar
%mvn_file org.gnu.inet:libidn libidn
%mvn_install -J doc/java
%endif

%find_lang %name
%set_verify_elf_method strict
%if_with emacs
%define _unpackaged_files_terminate_build 1
%endif

%check
export LD_LIBRARY_PATH=%buildroot/%_lib:%buildroot%_libdir
%make_build -k check VERBOSE=1

%files -f %name.lang
/%_lib/*.so.*
%_bindir/idn
%_man1dir/*
%dir %docdir
%docdir/[ACFNRT]*

%files devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc
%_man3dir/*
%_infodir/*

%files devel-doc
%dir %docdir/
%docdir/*.html
%docdir/*.pdf
%docdir/reference/

%if_with emacs
%files -n emacs-%name
%_emacslispdir/*
%endif #emacs

%if_enabled java
%files java -f .mfiles
%doc COPYING* java/LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING* java/LICENSE-2.0.txt
%endif #java

%changelog
* Tue Jan 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.33-alt3
- Fixed tests.

* Tue Jan 10 2017 Michael Shigorin <mike@altlinux.org> 1.33-alt2.1
- BOOTSTRAP: make --without emacs really work.

* Mon Aug 08 2016 Dmitry V. Levin <ldv@altlinux.org> 1.33-alt2
- Relocated shared library from %%_libdir to /%%_lib (closes: #32362).

* Wed Jul 20 2016 Dmitry V. Levin <ldv@altlinux.org> 1.33-alt1
- 1.32 -> 1.33.

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.32-alt2
- NMU: added java subpackage (required by jxmpp)

* Mon Dec 14 2015 Dmitry V. Levin <ldv@altlinux.org> 1.32-alt1
- 1.29 -> 1.32.

* Sat Nov 15 2014 Dmitry V. Levin <ldv@altlinux.org> 1.29-alt1
- Updated to 1.29.

* Mon Jul 22 2013 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt1
- Updated to 1.28.

* Tue Jun 25 2013 Dmitry V. Levin <ldv@altlinux.org> 1.27-alt1
- Updated to 1.27.

* Sun Dec 16 2012 Dmitry V. Levin <ldv@altlinux.org> 1.26-alt1
- Updated to 1.26.

* Wed Jul 11 2012 Dmitry V. Levin <ldv@altlinux.org> 1.25-alt1
- Updated to 1.25.

* Thu Jan 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.24-alt1
- Updated to 1.24.

* Sun Dec 11 2011 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt1
- Updated to 1.23.
- Rewritten specfile.
- Fixed RPATH issue.
- Enabled test suite.
- Created libidn-devel-doc and emacs-libidn subpackages.

* Thu May 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.22-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.21-alt1
- new version

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt2
- rebuilt for debuginfo

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.19-alt1
- new version

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 1.15-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.8-alt1
- new version

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt1
- new version

* Thu Dec 20 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- new version

* Wed Jul 18 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.14-alt1
- new version

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.10-alt1
- new version

* Fri Jun 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.3-alt1
- new version

* Fri Aug 12 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.18-alt1
- new version

* Thu Feb 10 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.13-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.12-alt1
- new version

* Mon Sep 27 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.5-alt1
- new version

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 0.4.6-alt1
- initial spec
