Name: devscripts
Version: 2.22.2
Release: alt2.qa1
Source: %{name}_%version.tar.xz
Source1: devscripts-po4a.conf
Patch: devscripts-uscan-no_ssl_namecheck.patch
License: GPLv2
Group: Development/Other
Url: http://packages.debian.org/devscripts
Summary: Scripts to make the life of a Debian Package maintainer easier

# Automatically added by buildreq on Mon Jun 20 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error perl perl-Dpkg perl-Encode perl-Encode-Locale perl-File-Which perl-HTTP-Date perl-HTTP-Message perl-Locale-gettext perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Pod-Usage perl-Tie-RefHash perl-Time-Piece perl-Try-Tiny perl-URI perl-parent perl-podlators pkg-config python3 python3-base python3-dev sh4 xml-common xz
BuildRequires: docbook5-style-xsl dpkg help2man perl-File-HomeDir perl-JSON-PP perl-Pod-Checker perl-String-ShellQuote perl-autodie perl-libwww po4a python3-module-setuptools xsltproc

BuildRequires: perl-DB_File perl-HTTP-Tiny perl-File-DesktopEntry perl-Git-Wrapper perl-List-Compare perl-Moo perl-IPC-Run perl-TimeDate perl-GitLab-API-v4 perl-File-DirList perl-File-Touch perl(JSON.pm)

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

%package -n python3-module-%name
Group: Development/Other
Summary: Python3 bingings for %name
Buildarch: noarch
%description -n python3-module-%name
Python3 bingings for %name, %summary

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
sed -i 's/ --install-layout=deb//' scripts/Makefile

%build
%make COMPL_DIR=%_datadir/bash-completion/completions

%install
mkdir -p %buildroot/%_bindir \
	%buildroot/%prefix/lib/devscripts \
	%buildroot/%_datadir/devscripts \
	%buildroot/%_man1dir \
	%buildroot/%_man5dir \
	%buildroot/%perl_vendorlib \
	%buildroot/%_datadir/bash-completion/completions

%makeinstall DESTDIR=%buildroot  COMPL_DIR=%_datadir/bash-completion/completions

install */*.1 %buildroot/%_man1dir/
install */*.5 %buildroot/%_man5dir/
install -D cowpoke.conf %buildroot%_sysconfdir/cowpoke.conf

# XXX
cp -r lib/Devscripts %buildroot/%perl_vendorlib/
touch %buildroot%_sysconfdir/cvsdeb.conf

# Fix dmd conflict
mv %buildroot/%_man1dir/dget.1 %buildroot/%_man1dir/dget-debian.1
mv %buildroot/%_bindir/dget %buildroot/%_bindir/dget-debian

%files
%doc README*
%exclude %_defaultdocdir/%name
%_bindir/*
%_mandir/man*/*
%prefix/lib/devscripts
%_datadir/devscripts
%_datadir/bash-completion/completions/*
%perl_vendorlib/Devscripts
%config %_sysconfdir/[^b]*
%exclude %_bindir/checkbashisms
%exclude %_man1dir/checkbashisms.1*
%exclude %_datadir/bash-completion/completions/checkbashisms
%exclude %_datadir/bash-completion/completions/bts

%files -n checkbashisms
%_bindir/checkbashisms
%_man1dir/checkbashisms.1*
%_datadir/bash-completion/completions/checkbashisms

%add_python3_req_skip apt debian debian.changelog
%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 2.22.2-alt2.qa1
- NMU: fixed build

* Tue Aug 23 2022 Fr. Br. George <george@altlinux.org> 2.22.2-alt2
- Rename rarely used dget in the sake of dmd (Closes: #43534)

* Mon Jun 20 2022 Fr. Br. George <george@altlinux.org> 2.22.2-alt1
- Autobuild version bump to 2.22.2

* Mon Jan 24 2022 Alexander Danilov <admsasha@altlinux.org> 2.19.7-alt2
- FTBFS: add in BuildRequires xsltproc

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 2.19.7-alt1
- Autobuild version bump to 2.19.7

* Tue Feb 26 2019 Fr. Br. George <george@altlinux.ru> 2.19.3-alt2
- REmove conflict woth bash-completion

* Mon Feb 18 2019 Fr. Br. George <george@altlinux.ru> 2.19.3-alt1
- Autobuild version bump to 2.19.3

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.19.2-alt1_4
- fc merge, fixed checkbashisms hook

* Thu Nov 29 2018 Fr. Br. George <george@altlinux.ru> 2.18.9-alt1
- Version bump to 2.18.9

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.7-alt1_1
- new version

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.3-alt1_4
- update to new release by fcimport

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.3-alt1_1
- new version - checkbashisms that works

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 2.15.1-alt1
- Autobuild version bump to 2.15.1

* Tue Dec 16 2014 Fr. Br. George <george@altlinux.ru> 2.14.11-alt1
- Autobuild version bump to 2.14.11

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 2.14.10-alt1
- Autobuild version bump to 2.14.10

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.6-alt2.1
- Fixed build

* Wed Oct 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.12.6-alt2
- Fix build with new pod2man.

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 2.12.6-alt1
- Autobuild version bump to 2.12.6

* Thu Nov 15 2012 Fr. Br. George <george@altlinux.ru> 2.12.5-alt1
- Autobuild version bump to 2.12.5
- Hack in old po4a config file

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 2.12.4-alt1
- Autobuild version bump to 2.12.4

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.12.1-alt1
- Autobuild version bump to 2.12.1

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

