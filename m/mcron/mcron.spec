#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: mcron
Summary: a program to run tasks at regular (or not) intervals
Version: 1.1.1
Release: alt1
License: %gpl3plus
Group: System/Servers
BuildRequires: guile22-devel help2man makeinfo perl-unicore help2man
BuildPreReq: rpm-build-licenses
Url: https://www.gnu.org/software/mcron/
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Source2: %name.watch
Patch1: %name-%version.patch

%description
a program to run tasks at regular (or not) intervals


%prep
%setup
%patch1 -p1
chmod a+x build-aux/git-version-gen
%autoreconf
export PATH="$PATH:/usr/sbin"
sed -i 's!^SENDMAIL *=.*!SENDMAIL = /usr/sbin/sendmail -FCronDaemon -odi -oem!' Makefile.in
export SENDMAIL=/usr/sbin/sendmail
%configure

%build
%make

%install
%make_install DESTDIR=%buildroot INSTALL_PREFIX=%buildroot install

%files
%_bindir/mcron
%_infodir/mcron.*
%_man1dir/mcron.1.*
%guile_ccachedir/%name
/usr/share/guile/site/*/%name

%changelog
* Sat Jun 09 2018 Denis Smirnov <mithraen@altlinux.ru> 1.1.1-alt1
- first build for Sisyphus

