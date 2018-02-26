%def_enable pam_userpass

Summary: checkpassword-style PAM authentication program
Name: checkpassword-pam
Version: 0.99
Release: alt2
License: GPL
Group: System/Base
Source: %{name}-%{version}.tar
Source1: checkpassword-pam.pam
Source2: README.ALT
Patch: %name-%version-%release-alt-changes.patch
URL: http://checkpasswd-pam.sourceforge.net/

BuildRequires: libpam0-devel
%{?_enable_pam_userpass:BuildRequires: pam_userpass-devel}

%description
This program, when given a username and password through the
checkpassword interface (http://cr.yp.to/checkpwd/interface.html),
checks that username and password, and executes a program that has to
be authenticated.
%if_enabled pam_userpass
checkpassword-pam is built with pam_userpass.so. see README.ALT.
%endif

%prep
%setup
%patch -p1

%build
%autoreconf
%configure %{subst_enable pam_userpass}
%make

%install
%makeinstall_std
%if_enabled pam_userpass
install -m644 -D %SOURCE1 %buildroot%_defaultdocdir/%name-%version/%name.pam-config
install -m644 -D %SOURCE2 %buildroot%_defaultdocdir/%name-%version/README.ALT
%endif
install -m644 -D README %buildroot%_defaultdocdir/%name-%version/README
install -m644 -D interface.html %buildroot%_defaultdocdir/%name-%version/interface.html

%files
%_defaultdocdir/%name-%version
%attr(2711,root,auth) %_bindir/checkpassword-pam
%_man8dir/*

%changelog
* Sat Feb 12 2011 Afanasov Dmitry <ender@altlinux.org> 0.99-alt2
- add alt-changes patch with pam_userpass support
- add docs (e.g. interface.html)

* Tue Aug 25 2009 Boris Savelev <boris@altlinux.org> 0.99-alt1
- initial build

