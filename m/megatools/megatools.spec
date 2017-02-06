Name: megatools
Version: 1.9.98
Release: alt1%ubt
Summary: Command line client for MEGA
License: GPLv3+
Url: http://megatools.megous.com/
Group: Archiving/Backup
Source0: %name-%version.tar
BuildRequires(pre): rpm-build-ubt
BuildRequires: libfuse-devel, libcurl-devel, openssl-devel, glib2-devel, libgmp-devel
BuildRequires: gobject-introspection-devel, asciidoc-a2x

%description
Megatools is a collection of programs for accessing Mega service from a command
line of your desktop or server.

Megatools allow you to copy individual files as well as entire directory trees
to and from the cloud. You can also perform streaming downloads for example to
preview videos and audio files, without needing to download the entire file.
You can register account using a "megareg" tool, with the benefit of having
true control of your encryption keys.
Megatools are robust and optimized for fast operation - as fast as Mega servers
allow. Memory requirements and CPU utilization are kept at minimum.

%prep
%setup

%build
autoreconf -fisv
%configure	--disable-silent-rules
sed -i 's/\(GLIB_CFLAGS = \)-pthread/\1/' Makefile
export LD_LIBRARY_PATH=$PWD/.libs
%make

%install
%makeinstall_std
%files
%doc HACKING NEWS README LICENSE
%_bindir/mega*
%_mandir/man1/mega*.1.*
%_mandir/man5/megarc.5.*
%_mandir/man7/%name.7.*

%changelog
* Mon Feb 06 2017 Anton Farygin <rider@altlinux.ru> 1.9.98-alt1%ubt
- first build for ALT
