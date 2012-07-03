Name: rpm-build-vala
Version: 0.3
Release: alt1

Summary: RPM helper macros and dependency utils to build Vala packages
License: GPL
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch

%description
These helper macros and dependency calculation utils facilitate creation of
RPM packages containing GObject Introspection files.

%prep
%setup

%install
mkdir -p %buildroot{%_rpmlibdir,%_rpmmacrosdir}
install -pD -m644 rpm-build-vala.macros %buildroot%_rpmmacrosdir/vala
install -pD -m644 vala-files.req.list %buildroot%_rpmlibdir/vala-files.req.list
for f in vala.req* vala.prov* ; do
  install -m755 -p "$f" "%buildroot%_rpmlibdir/$f"
done


%files
%_rpmmacrosdir/vala
%_rpmlibdir/vala*

%changelog
* Tue Mar 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- change vala to vapi-common in vala-files.req.list
- only one dir /usr/share/vala/vapi for third-party *.vapi files

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update for vala-0.14 and vala-0.16

* Fri Jun 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- Initial release
