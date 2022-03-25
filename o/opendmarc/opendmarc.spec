Name: opendmarc
Version: 1.4.1.1
Release: alt1
Summary: A Domain-based Message Authentication, Reporting & Conformance (DMARC) milter and library

License: BSD and Sendmail
Group: System/Servers
URL: http://www.trusteddomain.org/opendmarc.html

Source0: https://github.com/trusteddomainproject/OpenDMARC/archive/refs/tags/rel-opendmarc-1-4-1-1.tar.gz
Source1: %name.sysconfig
Source2: %name.service
Patch1: opendmarc-1.4.0-ticket159-179.patch
Patch2: opendmarc-1.4.1-conf_holdquarantinedmessages.patch
Patch3: https://patch-diff.githubusercontent.com/raw/trusteddomainproject/OpenDMARC/pull/178.patch
Patch4: opendmarc-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libbsd-devel
BuildRequires: libmariadb-devel
BuildRequires: libspf2-devel
BuildRequires: openssl-devel
BuildRequires: perl-DBI
BuildRequires: perl-IO-Compress
BuildRequires: perl-JSON
BuildRequires: perl-MIME-tools
BuildRequires: perl-PerlIO-gzip
BuildRequires: perl-Switch
BuildRequires: perl-XML-Simple
BuildRequires: sendmail-devel
Requires(pre): shadow-utils

%description
OpenDMARC (Domain-based Message Authentication, Reporting & Conformance)
provides an open source library that implements the DMARC verification
service plus a milter-based filter application that can plug in to any
milter-aware MTA, including sendmail, Postfix, or any other MTA that supports
the milter protocol.

The DMARC sender authentication system is still a draft standard, working
towards RFC status.

The database schema required for some functions is provided in
%_datadir/%name/db. The rddmarc tools are provided in
%_datadir/%name/contrib/rddmarc.

%package -n libopendmarc
Summary: An open source DMARC library
Group: System/Libraries

%description -n libopendmarc
This package contains the library files required for running services built
using libopendmarc.

%package -n libopendmarc-devel
Summary: Development files for libopendmarc
Group: Development/C

%description -n lib%name-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopendmarc.

%prep
%setup -n OpenDMARC-rel-opendmarc-1-4-1-1
%autopatch -p1

%build
%autoreconf
%configure \
	--with-sql-backend \
	--with-spf \
	--with-spf2-include=%_includedir/spf2 \
	--with-spf2-lib=%_libdir/libspf2.so
%make_build

%install
%makeinstall_std

install -Dpm 0644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -Dpm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
mkdir -p -m 0755 %buildroot%_sysconfdir/%name

# Install and set some basic settings in the default config file
install -m 0644 %name/%name.conf.sample %buildroot%_sysconfdir/%name.conf

sed -i 's|^# AuthservID name |AuthservID HOSTNAME |' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# HistoryFile /var/run/%name.dat|# HistoryFile %_spooldir/%name/%name.dat|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# Socket |Socket |' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# SoftwareHeader false|SoftwareHeader true|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# SPFIgnoreResults false|SPFIgnoreResults true|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# SPFSelfValidate false|SPFSelfValidate true|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# Syslog false|Syslog true|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# UMask 077|UMask 007|' %buildroot%_sysconfdir/%name.conf
sed -i 's|^# UserID %name|UserID %name:mail|' %buildroot%_sysconfdir/%name.conf
sed -i 's|/usr/local||' %buildroot%_sysconfdir/%name.conf

install -p -d %buildroot%_tmpfilesdir
echo "D /run/%name 0700 %name %name -" > %buildroot%_tmpfilesdir/%name.conf

rm -rf %buildroot%_prefix/share/doc/%name
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/*.a

mkdir -p %buildroot%_includedir/%name
install -m 0644 lib%name/dmarc.h %buildroot%_includedir/%name/

mkdir -p %buildroot%_spooldir/%name
mkdir -p %buildroot/run/%name

# install db/ and contrib/ to datadir
mkdir -p %buildroot%_datadir/%name/contrib
cp -R db/ %buildroot%_datadir/%name
sed -i -e 's:/usr/local/bin/python:%__python3:' contrib/rddmarc/dmarcfail.py
cp -R contrib/rddmarc/ %buildroot%_datadir/%name/contrib
# not much point including the Makefiles
rm -f %buildroot%_datadir/%name/contrib/rddmarc/Makefile*
rm -f %buildroot%_datadir/%name/db/Makefile*

mkdir -p %buildroot%_defaultdocdir/libopendmarc-devel-%version
cp -a lib%name/docs/*.html %buildroot%_defaultdocdir/libopendmarc-devel-%version

%pre
getent group %name >/dev/null || groupadd -r %name
getent passwd %name >/dev/null || \
	useradd -r -g %name -G mail -d /run/%name -s /sbin/nologin \
	-c "OpenDMARC Milter" %name
exit 0

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README RELEASE_NOTES LICENSE LICENSE.Sendmail
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_datadir/%name
%_sbindir/*
%_mandir/*/*
%dir %attr(-,%name,%name) %_spooldir/%name
%dir %attr(710,%name,mail) /run/%name
%dir %attr(-,%name,%name) %_sysconfdir/%name

%files -n libopendmarc
%_libdir/lib%name.so.*

%files -n libopendmarc-devel
%doc %_defaultdocdir/libopendmarc-devel-%version
%_includedir/%name
%_libdir/*.so

%changelog
* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.1.1-alt1
- Initial build for Sisyphus (based on spec from Fedora) (ALT #42230).

