Name: polkit-pkla-compat
Version: 0.1
Release: alt1

Summary: Rules for polkit to add compatibility with pklocalauthority
Group: System/Libraries
License: LGPLv2+
Url: https://fedorahosted.org/polkit-pkla-compat/

Source: https://fedorahosted.org/releases/p/o/%name/%name-%version.tar.xz

PreReq: polkit
Conflicts: polkit < 0.105

BuildRequires: glib2-devel >= 2.34 libpolkit-devel >= 0.105
BuildRequires: docbook-style-xsl xsltproc

%description
A polkit JavaScript rule and associated helpers that mostly provide
compatibility with the .pkla file format supported in polkit <= 0.105
for users of later polkit releases.

%prep
%setup

%build
%configure \
    --localstatedir=%_var \
    --with-polkitd-group=polkitd

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/pkla-admin-identities
%_bindir/pkla-check-authorization
%dir %attr(0750,root,polkitd) %dir %_sysconfdir/polkit-1/localauthority
%dir %_sysconfdir/polkit-1/localauthority/*.d
%dir %_sysconfdir/polkit-1/localauthority.conf.d
%config(noreplace) %_sysconfdir/polkit-1/rules.d/49-polkit-pkla-compat.rules
%dir %attr(0750,root,polkitd) %_localstatedir/polkit-1
%dir %_localstatedir/polkit-1/localauthority
%dir %_localstatedir/polkit-1/localauthority/*.d
%_man8dir/pkla-admin-identities.8*
%_man8dir/pkla-check-authorization.8*
%_man8dir/pklocalauthority.8*

%doc AUTHORS NEWS README

%changelog
* Fri May 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- adapted for Sisyphus

* Thu May  9 2013 Miloslav Trmač <mitr@redhat.com> - 0.1-2
- Add a comment above License about SRPM-only licenses
- Reword Summary: to avoid a rpmlint warning
- Move INSTALL= to the %%install section

* Tue May  7 2013 Miloslav Trmač <mitr@redhat.com> - 0.1-1
- Initial package
