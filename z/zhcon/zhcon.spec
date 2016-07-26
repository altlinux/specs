# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libggi-devel libpth-devel
# END SourceDeps(oneline)
%define fedora 24
Name: zhcon
Summary: A Fast Console CJK System Using FrameBuffer
Version: 0.2.6
Release: alt1_29
Group: File tools
License: GPLv2+
URL:   http://zhcon.sourceforge.net/
Source0: http://ftp.debian.org/debian/pool/main/z/zhcon/%{name}_%{version}.orig.tar.gz
Patch0: http://ftp.debian.org/debian/pool/main/z/zhcon/%{name}_%{version}-6.1.diff.gz
Patch1: %{name}-%{version}-flags.patch
Patch2: %{name}-%{version}-path-define.patch
Patch3: %{name}-%{version}-gcc43.patch
Patch4: %{name}-%{version}-locale.patch
Patch5: %{name}-%{version}-keyswitch.patch
Patch6: %{name}-%{version}-xf86int10.patch
Summary: A fast Linux Console Chinese System that supports framebuffer
Summary(zh_CN): Zhcon 是一个支持 Framebuffer 的 Linux 中日韩文控制台
Summary(zh_TW): Zhcon 是一個支援 Framebuffer 及多內碼 Linux 中日韓文主控台

%if 0%{?fedora} >= 9
%define ncurse_libs_postfix -libs
%endif


BuildRequires: autoconf-common automake-common 
BuildRequires: gettext-tools libasprintf-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libgpm-devel
Requires: gpm gpm-root termutils
Source44: import.info


%description
Zhcon is a fast Linux Console Chinese System which supports
framebuffer device.It can display Chinese, Japanese or Korean
double byte characters. Supported language encodings include:
UTF8, GB2312, GBK, BIG5, JIS and KSC.

%description -l zh_CN
zhcon 是一个支持 Framebuffer 的 Linux 中日韩文控制台。
它能够控制台上显示简体中文、繁体中文、日文、韩文
等双字节字符。支持多种输入法。
现支持的有： UTF8, GB2312, GBK, BIG5, JIS 及 KSC。

%description -l zh_TW
zhcon 是一個支援 Framebuffer 與多内碼的 Linux 中日韓文主控台。
它能够在控制台上顯示簡體中文、繁體中文、日文、韓文
等雙位元組字元。支援多种输入法。
現支援的內碼有： UTF8, GB2312, GBK, BIG5, JIS 及 KSC。
%prep
%setup -q
%patch0 -p1 -b .6-diff
%patch1 -p1 -b .flags
%patch2 -p0 -b .path-define
%patch3 -p0 -b .gcc43
%patch4 -p0 -b .locale
%patch5 -p0 -b .keyswitch
%patch6 -p0 -b .xf86int10
iconv -f GB2312 -t UTF-8 ChangeLog -o ChangeLog.utf && mv -f ChangeLog.utf ChangeLog
( cd doc; tar -zxf html.tar.gz; chmod 755 manual)
# liu5 is a non-free input method
rm -f input/big5-liu5.mb

%build
# exit if bootstrap fails
# missing config.rpath causes automake failure
sed -i -e 's|set -x|set -e -x|' bootstrap
touch config.rpath

./bootstrap
autoreconf -ivf
%global _hardened_build 1

%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -c -p" install

%files
%doc AUTHORS ChangeLog COPYING README README.utf8 THANKS TODO doc/bpsf.txt doc/README.html
%lang(zh_CN) %doc doc/manual* doc/poem.gb doc/poem.gb.utf8
%lang(zh_TW) %doc doc/poem.big5
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(4711,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_29
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_28
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_26
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_25
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_24
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_23
- update to new release by fcimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_22
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_21
- update to new release by fcimport

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_20
- new release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_19
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_18
- update to new release by fcimport

* Sun Jul 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_17
- initial release by fcimport

