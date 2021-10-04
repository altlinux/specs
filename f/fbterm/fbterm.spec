# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libgpm-devel pkgconfig(freetype2)
# END SourceDeps(oneline)
%ifarch x86_64 %ix86
BuildRequires: libx86-devel
%endif
BuildRequires: termutils-devel terminfo-extra
%define fedora 21
Name: fbterm
Version: 1.7
Release: alt3.qa1
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: File tools
Url: http://code.google.com/p/fbterm/
#http://fbterm.googlecode.com/files/%%name-%%version.tar.gz
Source0: %name-%version.tar.gz

#Patch0:    %name-1.2-kernel-header.patch
#Patch1:    %name-1.3-setcap.patch
#Patch2:    %name-1.4-iminput.patch
#Patch3:    %name-1.6-rpmpack.patch
#Patch4:    %name-1.6-el5.patch
Patch5:    %name-%version-alt-build.patch

Summary: A frame-buffer terminal emulator
Summary(zh_CN): 运行在帧缓冲的快速终端仿真器
Summary(zh_TW): 運行在frame-buffer的快速終端模擬機

%define fbterm_rules_name 99-fbterm.rules
%define fbterm_rules_dir %_sysconfdir/udev/rules.d
%define fbterm_rules_path %fbterm_rules_dir/%fbterm_rules_name

BuildRequires: autoconf automake
BuildRequires: fontconfig-devel gpm-devel
Requires: fontconfig
Source44: import.info

%description
FbTerm is a fast terminal emulator for Linux with frame-buffer device.
Features include:
- mostly as fast as terminal of Linux kernel while accelerated scrolling
  is enabled on frame-buffer device
- select font with fontconfig and draw text with freetype2, same as
  Qt/Gtk+ based GUI apps
- dynamically create/destroy up to 10 windows initially running default
  shell
- record scroll back history for every window
- auto-detect text encoding with current locale, support double width
  scripts like  Chinese, Japanese etc
- switch between configurable additional text encodings with hot keys
  on the fly
- copy/past selected text between windows with mouse when gpm server
  is running

%if 0%{?fedora} >= 9
%package udevrules
Group: File tools
Summary: udev rules that grant regular user access
Requires: udev

%description udevrules
Regular users might use some applications that require access to frame-buffer device.
For example, ibus-fbterm requires access to /dev/fb0.
This sub-package enables regular user for such access.
%endif

%prep
%setup
#%patch0 -p0 -b .kernel-header
#%patch1 -p0 -b .setcap
#%patch2 -p0 -b .iminput
#%patch3 -p0 -b .rpmpack
#%if 0%{?fedora} >= 9
#%else
#%patch4 -p0 -b .el5
#%endif
%patch5 -p2

%build
autoreconf -iv
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
# fbterm info
mkdir -p %buildroot/usr/share/terminfo/f
export TERMINFO=%buildroot/usr/share/terminfo
%__make DESTDIR=%buildroot install
%__chmod 755 %buildroot/%_bindir/%name
%if 0%{?fedora} >= 9
%__mkdir -p %buildroot/%fbterm_rules_dir
%__cat >>%buildroot/%fbterm_rules_path <<EOF
KERNEL=="fb[0-9]*", SUBSYSTEM=="graphics", MODE="0666"
EOF
%endif

%if 0%{?fedora} >= 9
%post
[ -x /sbin/setcap ] && setcap 'cap_sys_tty_config+ep' %_bindir/%name ||:
%endif

%files
%doc AUTHORS ChangeLog COPYING README
%if 0%{?fedora} >= 9
%_bindir/%name
%else
%attr(4711,root,root) %_bindir/%name
%endif
%_mandir/man1/%name.1*
/usr/share/terminfo/f/fbterm

%if 0%{?fedora} >= 9
%files udevrules
%config(noreplace) %fbterm_rules_path
%endif

%changelog
* Tue Oct 05 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7-alt3.qa1
- Fixed build on aarch64 and ppc64le.

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt3
- Updated build for gcc-6

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 1.7-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_4
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1
- initial fc import

