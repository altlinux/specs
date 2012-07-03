Name: mod_limitipconn
Version: 0.04
Release: alt3

Summary: Limit simultaneous connections by an IP address
License: X11
Group: System/Servers

Url: http://dominia.org/djao/limitipconn.html
Source0: http://dominia.org/djao/limit/mod_limitipconn-0.04.tar.gz
Source1: http://dominia.org/djao/limit/contrib/mc/README
Patch0: http://dominia.org/djao/limit/contrib/kei-lc/mod_limitipconn_local_IP_patch.diff
Patch1: http://dominia.org/djao/limit/contrib/mc/mod_limitipconn-0.04-vhost.patch

Packager: Michael Shigorin <mike@altlinux.ru>

# Automatically added by buildreq on Thu Feb 22 2007
BuildRequires: apache-devel

%description
The mod_limitipconn module lets you enforce limits on the number of
simultaneous downloads allowed from a single IP address. You can also
control which MIME types are affected by the limits.

%prep
%setup
#patch0 -p0
%patch1 -p1

%build
%apache_apxs -c %name.c

%install
install -pD -m644 %name.so %buildroot%_libdir/apache/%name.so

%files
%doc README ChangeLog
%_libdir/apache/%name.so

# TODO:
# - conditional patch application

%changelog
* Thu Feb 22 2007 Michael Shigorin <mike@altlinux.org> 0.04-alt3
- added patches from project page (mutually exclusive):
  + LocalIP (by Chan Leung) to exempt given IP address (not applied)
  + MaxConnPerUid/MaxConnPerVhost/MaxLA{1,5,15} (by Maxim Chirkov)
    to limit also by user, vhost, or load average (applied)

* Sun Aug 21 2005 Michael Shigorin <mike@altlinux.org> 0.04-alt2
- rebuilt for Sisyphus

* Tue Aug 03 2004 Michael Shigorin <mike@altlinux.ru> 0.04-alt1
- built for ALT Linux

