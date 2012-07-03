%define major 1.8

Name: wavesurfer
Version: %major.5
Release: alt3

%add_tcl_req_skip tile
%add_tcl_lib_path %_datadir/%name
%set_tcl_req_method strict

Summary: WaveSurfer is a tool for sound visualization and manipulation
License: BSD
Group: Sound
URL: http://www.speech.kth.se/%name/

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl  
BuildRequires: iconv tcl
BuildArch: noarch

%description
%name is an Open Source tool for sound visualization and manipulation.
It has been designed to suit both novice and advanced users. WaveSurfer has
a simple and logical user interface that provides functionality in an intuitive
way and which can be adapted to different tasks. It can be used as a stand-alone
tool suited for a wide range of tasks in speech research and education, but is also
a platform for more advanced applications. WaveSurfer can be extended through
plug-ins. It is also possible to embedded it in other applications or to control
it remotely.

%prep
%setup

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/%name/{plugins,configurations,msgs}
# rearrange a bit executables
cat <<EOF > %buildroot%_bindir/%name
#!/bin/sh
#\\
exec wish "\$0" "\$@"
source %_datadir/%name/%name.tcl
EOF
cat <<EOF > %buildroot%_bindir/wsurf-createshapes
#!/bin/sh
#\\
exec wish "\$0" "\$@"
source %_datadir/%name/createshapes.tcl
EOF
chmod +x %buildroot%_bindir/*

# next two in own packages
rm -f wsurf%major/cmdline.tcl wsurf%major/tkcon.tcl
# library, tools, plugins, configs
install -p -m0644 wavesurfer.tcl tools/*.tcl wsurf%major/*.tcl %buildroot%_datadir/%name
install -p -m0644 wsurf%major/plugins/*.plug %buildroot%_datadir/%name/plugins
install -p -m0644 wsurf%major/configurations/*.conf %buildroot%_datadir/%name/configurations
grep -vE 'cmdline|tkcon' < wsurf%major/pkgIndex.tcl > %buildroot%_datadir/%name/pkgIndex.tcl

# menus, icons
install -p -m0644 -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -p -m0644 -D icons/ws48.xpm %buildroot%_niconsdir/%name.xpm

# msgcat expects contents in utf-8
iconv -f iso8859-1 -t utf-8 msgs/se.msg > %buildroot%_datadir/%name/msgs/se.msg
cat msgs/ru_ru.koi8-r.msg ru.msg |grep -v Silence |%__sed 's| ru_ru.koi8-r | ru |' |\
iconv -f koi8-r -t utf-8 > %buildroot%_datadir/%name/msgs/ru.msg
chmod 0644 %buildroot%_datadir/%name/msgs/*.msg

# cleanups
chmod 0644 README*

# python go away 
rm -f demos/*.py

%files
%doc README* LICENSE*
%doc doc demos
%_bindir/*
%_datadir/%name
%_niconsdir/*
%_desktopdir/%name.desktop

%changelog
* Sun Jan 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.5-alt3
- reqs on aoss removed

* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.5-alt2
- rebuilt

* Mon Jul 24 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.5-alt1
- 1.8.5

* Thu Jul 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Fri Dec 24 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Fri Dec 12 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.7-alt1
- 1.5.7

* Sat Jul 12 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.5.2-alt1
- 1.5.2

* Tue Mar 11 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.4.7-alt1
- 1.4.7
- http proxy support added

* Tue Jan 14 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.4.6-alt1
- 1.4.6

* Tue Oct  8 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.4-alt1
- 1.4.4

* Wed Jun  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4-alt3
- moved to %_tcldatadir

* Sat May 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4-alt1
- 1.4

* Wed Nov 28 2001  <s.bolshakov@belcaf.com> 1.1-alt1
- First spec file for ALT Linux distribution.

