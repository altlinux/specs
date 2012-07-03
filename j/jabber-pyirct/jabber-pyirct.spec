Name: jabber-pyirct
Version: 0.4
Release: alt1

Summary: IRC transport for XMPP servers
License: GPL
Group: System/Servers
Url: http://sourceforge.net/projects/xmpppy/files/PyIRCt/
Packager: Alexey Gladkov <legion@altlinux.org>

Requires(pre): shadow-utils jabber-common
Requires(post): %post_service
Requires(preun): %preun_service

Provides: pyirc-t = %version-%release

BuildRequires: jabber-common python-devel

Source0: irc-transport-%version.tar
Source1: pyirct.adapter
Source2: pyirct.init
Source3: pyirct.logrotate
Source4: pyirct.xml

%description
%name is a IRC transport for Jabber servers.

%prep
%setup -n irc-transport-%version

%install
mkdir -p -- \
	%buildroot%_initdir \
	%buildroot%_libdir/pyirct  \
	%buildroot%_var/run/pyirct \
	%buildroot%_var/log/pyirct \
	%buildroot%_spooldir/pyirct

cp -a *.py %buildroot%_libdir/pyirct/

sed -e 's,@LIBDIR@,%_libdir,g' \
	%_sourcedir/pyirct.init > %buildroot%_initdir/%name
chmod +x %buildroot%_initdir/%name

install -pm 0755 -D %_sourcedir/pyirct.adapter   %buildroot%_jabber_component_dir/pyirct
install -pm 0640 -D %_sourcedir/pyirct.xml       %buildroot%_sysconfdir/pyirct.xml
install -pm 0640 -D %_sourcedir/pyirct.logrotate %buildroot%_sysconfdir/logrotate.d/pyirct

%add_python_lib_path %_libdir/pyirct
%set_python_req_method strict

%pre
/usr/sbin/groupadd -r -f _pyirct &>/dev/null ||:
/usr/sbin/useradd -r -g _pyirct -d /dev/null -s /dev/null \
    -c "IRC Jabber transport" -M -n _pyirct &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc ChangeLog README.txt
%_initdir/%name
%_libdir/pyirct
%_jabber_component_dir/pyirct

%attr(0640,root,_pyirct) %config(noreplace) %_sysconfdir/pyirct.xml
%attr(640,root,root)     %config %_sysconfdir/logrotate.d/pyirct
%attr(0770,root,_pyirct) %dir %_spooldir/pyirct
%attr(0770,root,_pyirct) %dir %_var/run/pyirct
%attr(0770,root,_pyirct) %dir %_var/log/pyirct

%changelog
* Sat Dec 24 2011 Alexey Gladkov <legion@altlinux.ru> 0.4-alt1
- Initial build.
