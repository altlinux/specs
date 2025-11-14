%define _unpackaged_files_terminate_build 1

Name: squidclamav
Version: 7.3
Release: alt1
Summary: HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://github.com/darold/squidclamav
Vcs: http://squidclamav.darold.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: c-icap-devel
BuildRequires: gcc
BuildRequires: libarchive-devel
BuildRequires: ocaml-camlbz2-devel
BuildRequires: libssl-devel
BuildRequires: libtool
BuildRequires: zlib-devel
BuildRequires: perl-CGI

Requires: c-icap
Requires: squid
Requires: httpd

%description
%name is an antivirus for Squid proxy based on the Awards winnings ClamAv
anti-virus toolkit. Using it will help you securing your home or enterprise
network web traffic. %name is the most efficient Squid Redirector and
ICAP service antivirus tool for HTTP traffic available for free, it is written
in C and can handle thousand of connections. The way to add more securing on
your network for free is here.

%prep
%setup
%autopatch -p1

%build
#export CFLAGS="%optflags"
%configure \
  --disable-static \
  --enable-shared \
  --with-c-icap \
  --with-libarchive
%make 
%make_build

%install
%makeinstall_std
rm -fr %buildroot%_datadir/%name

%files
%doc README NEWS INSTALL 
%defattr(-,root,root)
%dir %_datadir/c_icap/templates/%name
%_datadir/c_icap/templates/%name/en
%config(noreplace) %_sysconfdir/squidclamav.conf
%_libdir/c_icap/squidclamav.*
%_libexecdir/%name/
%_man1dir/%name.*
%_sysconfdir/squidclamav.conf.default
%attr(0644,root,root) %_datadir/c_icap/templates/squidclamav/*/MALWARE_FOUND

%changelog
* Fri Nov 14 2025 Pavel Shilov <zerospirit@altlinux.org> 7.3-alt1
- Initial build for Sisyphus.