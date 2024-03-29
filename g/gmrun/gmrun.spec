%define _unpackaged_files_terminate_build 1

Name: gmrun
Version: 1.4w
Release: alt1
Summary: Small GTK based 'Run application'

Group: System/X11
License: Unlicense
Url: https://github.com/WdesktopX/gmrun
Source: %name-%version.tar

Packager: Afanasov Dmitry <ender@altlinux.org>

BuildRequires: gcc-c++ pkgconfig gettext
BuildRequires: libgtk+3-devel >= 3.14

%description
A full featured 'Run' application, GTK based.

%prep
%setup

%build
# xdg paths are disable for compatibility with old gmrun history
%configure \
    --enable-nls \
    --enable-gtk3 \
    --disable-xdg

%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_sysconfdir/%{name}rc
%_datadir/applications/%name.desktop
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_man1dir/%name.*
%_pixmapsdir/%name.*
%doc AUTHORS README.md ChangeLog

%changelog
* Sat Jul 16 2022 Andrew Savchenko <bircoph@altlinux.org> 1.4w-alt1
- Version bump (Closes: 42988).
- Move to new upstream.
- Add debuginfo.

* Fri May 08 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.2-alt3
- fix buidl with gcc4.4. gcc4.3 is not supported now

* Wed Oct 29 2008 Afanasov Dmitry <ender@altlinux.org> 0.9.2-alt2
- add debian patches
- fix gcc4.3 build

* Sat Sep 23 2006 Terechkov Evgenii <evg@altlinux.ru> 0.9.2-alt1
- Build for Sisyphus

* Sat Jul 15 2006 Terechkov Evgenii <evg@altlinux.ru> 0.9.2-alt0.C30.1
- Initial build for ALT

* Thu Aug 25 2005 Marius FERARU <altblue@n0i.net> 0.9.2-5.n0i.2
- rebuild

* Wed Jul 27 2005 Marius FERARU <altblue@n0i.net> 0.9.2-5.n0i.1
- rebuild

* Wed Nov 24 2004 Marius FERARU <altblue@n0i.net> 0:0.9.2-0.n0i.2
- automatic rebuild

* Mon Dec 29 2003 Marius FERARU <altblue@n0i.net> 0:0.9.2-0.n0i.1
- gmrun version 0.9.2
- Fedora-ized spec

* Sun Jun 22 2003 Marius FERARU <altblue@n0i.net> 0.9-0.n0i
- version 0.9

* Sat Jun 14 2003 Marius FERARU <altblue@n0i.net> 0.8.1-1.n0i
- rebuild on RHL9

* Thu Nov 21 2002 Marius FERARU <altblue@n0i.net> 0.8.1-0.n0i
- removed duplicate 'configure'
- 'files' section tweaks
- eliminated useles 'prefix' macro
- added smp flags to make
- changed 'group' to a more standardized one
- changed the-too-obstinate 'description'
- change the 'install' section to correctly install files
- added 'buildroot' macro

* Sat Aug 17 2002 Mihai Bazon <mishoo@infoiasi.ro>
- Some bugs fixed, specifically the behavior of END/HOME keys (or C-E, C-A),
  and the major one: you could not run a file that has an extension handler
  with some other program than the extension handler :)

* Fri Aug 16 2002 Mihai Bazon <mishoo@infoiasi.ro>
- Fixed bug: filenames can now contain white spaces (will be backslash-ed)
- New feature: can specify application handler per file extension, so you
  can directly type the name of some .cpp file and emacs will show up :)
  see config file for details.
- New feature: can automatically simulate a TAB press after some timeout.
  Check config file for details, key "TabTimeout" (0 to disable).
- New feature: you can now always use "system" for running programs
  (specify --enable-system at configure).

* Fri Oct 19 2001 Mihai Bazon <mishoo@infoiasi.ro>
- Fixed bug with sorting of completion list
- Fixed bug with URL handling
- New parameter: list of execs to be always run in terminal
- New feature: last history line appears directly in edit line, selected

* Wed Aug 01 2001 Mihai Bazon <mishoo@infoiasi.ro>
- Programs are now executed using execv.  We don't use system anymore, thus
  avoiding forking another shell.
- gmrun.spec gets now generated automagically, at ./configure.

* Sun Jul 22 2001 Mihai Bazon <mishoo@infoiasi.ro>
- added "!" history backward search; like in bash, it finds the last command
  which begins with the entered text.
- CTRL-R / CTRL-S don't show two identical consecutive records.

* Thu Jul 19 2001 Mihai Bazon <mishoo@infoiasi.ro>
- added history search capabilities (CTRL-R / CTRL-S, like in bash / Emacs)
- small bug fixes

* Fri Jun 29 2001 Mihai Bazon <mishoo@infoiasi.ro>
- history size configurable from config file
- window appears directly where it should (no more flicker)

* Wed May 14 2001 Mihai Bazon <mishoo@infoiasi.ro>
- added default configuration file (goes to /usr/share/gmrun)

* Wed May 07 2001 Marius Feraru <altblue@n0i.net>
- updated to version 0.5.3 and took over to 0.5.31

* Wed May 03 2001 Marius Feraru <altblue@n0i.net>
- updated to version 0.2.5 and took over to 0.2.51:
	* configuration file with 2 options for now:
		'Terminal' and 'Width'
	* added some more (and hopefully more useful) documentation:
		README.hints, README.gmrunrc and README.icewm

* Wed May 03 2001 Marius Feraru <altblue@n0i.net>
- updated to version 0.2.2:
	* Ctrl-Enter spawns a terminal

* Wed May 02 2001 Marius Feraru <altblue@n0i.net>
- initial RPM build
