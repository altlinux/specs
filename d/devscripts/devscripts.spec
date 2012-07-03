Name: devscripts
Version: 2.11.8
Release: alt1
Source: %{name}_%version.tar.gz
Patch: devscripts-uscan-no_ssl_namecheck.patch
License: GPLv2
Group: Development/Other
Url: http://packages.debian.org/devscripts
Summary: Scripts to make the life of a Debian Package maintainer easier

%setup_python_module %name

BuildRequires: python-module-setuptools

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: libgpg-error perl-Dpkg perl-Encode perl-File-BaseDir perl-HTTP-Date perl-HTTP-Message perl-Locale-gettext perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Text-CharWidth perl-Text-WrapI18N perl-TimeDate perl-URI perl-libnet perl-podlators python-base xml-common
BuildRequires: docbook5-style-xsl dpkg perl-DBM perl-File-DesktopEntry perl-libwww po4a xsltproc

%description
Devscripts provides several scripts which may be of use to Debian
developers.  The following gives a summary of the available scripts --
please read the manpages for full details about the use of these
scripts.  They are contributed by multiple developers; for details of
the authors, please see the code or manpages.

Also, many of these scripts have dependencies on other packages, but
rather than burden the package with a large number of dependencies,
most of which will not be needed by most people, the individual
dependencies are listed as "Recommends" in the control file.  This
ensures that the packages will be installed by default but allows
users to remove them if desired.  The dependencies and recommendations
are listed in square brackets in the description below, as well as in
the Description field in the control file.

%package -n %packagename
Group: Development/Other
Summary: Python bingings for %name
Buildarch: noarch
%description -n python-module-%name
Python bingings for %name, %summary

%package -n checkbashisms

Summary: Check shell scripts for common bash-specific contructs
Group: Development/Other
BuildArch: noarch

%description -n checkbashisms
checkbashisms checks whether a /bin/sh script contains any common
bash-specific contructs.
It is the part of the Debian devscripts package.

%prep
%setup
%patch -p0
sed -i 's/^[.]TQ/.TP/' scripts/diff2patches.1
grep -rl /usr/share/sgml/docbook/stylesheet/xsl/nwalsh/manpages/docbook.xsl . |
	while read N; do
		sed -i 's@/usr/share/sgml/docbook/stylesheet/xsl/nwalsh/manpages/docbook.xsl@/usr/share/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl@g' "$N"
	done
touch po4a/fr/deb-reversion.fr.1
sed -i 's/ --install-layout=deb//' scripts/Makefile

%build
%make

%install
mkdir -p %buildroot/%_bindir \
	%buildroot/%prefix/lib/devscripts \
	%buildroot/%_datadir/devscripts \
	%buildroot/%_man1dir \
	%buildroot/%_man5dir \
	%buildroot/%perl_vendorlib \
	%buildroot/%_sysconfdir/bash_completion.d

%makeinstall DESTDIR=%buildroot
install scripts/*.1 %buildroot/%_man1dir/
install scripts/*.5 %buildroot/%_man5dir/
install -D cowpoke.conf %buildroot%_sysconfdir/cowpoke.conf

# XXX
cp -r Devscripts %buildroot/%perl_vendorlib/
touch %buildroot%_sysconfdir/cvsdeb.conf

%files
%doc README*
%exclude %_defaultdocdir/%name
%_bindir/*
%_mandir/man*/*
%prefix/lib/devscripts
%_datadir/devscripts
%_sysconfdir/bash_completion.d/*
%perl_vendorlib/Devscripts
%config %_sysconfdir/[^b]*
%exclude %_bindir/checkbashisms
%exclude %_man1dir/checkbashisms.1*

%files -n checkbashisms
%_bindir/checkbashisms
%_man1dir/checkbashisms.1*

%files -n %packagename
%python_sitelibdir_noarch/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.11.8-alt1
- Autobuild version bump to 2.11.8

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 2.11.6-alt1
- Autobuild version bump to 2.11.6

* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 2.11.4-alt1
- Autobuild version bump to 2.11.4

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 2.11.3-alt1
- Autobuild version bump to 2.11.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.11.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 2.11.1-alt1
- Autobuild version bump to 2.11.1

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.11.0-alt3
- removed conflict with checkbashisms (integrated as subpackage)

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.11.0-alt2
- Implement SSL hostname check omitting

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 2.11.0-alt1
- Autobuild version bump to 2.11.0

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 2.10.72-alt1
- Autobuild version bump to 2.10.72

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.10.71-alt1
- Autobuild version bump to 2.10.71

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 2.10.70-alt1
- Autobuild version bump to 2.10.70

* Thu Dec 23 2010 Fr. Br. George <george@altlinux.ru> 2.10.69-alt1
- Initial build from deb

