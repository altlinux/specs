Name: installer-feature-kiosk-user
Version: 0.1
Release: alt2

Summary: Add/preconfigure kiosk user
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch
Requires: installer-common-stage3
Requires: autologin

%description
This package contains kiosk user preconfiguration hook
for installer stage3.

%install
mkdir -p %buildroot

%post
useradd -s /bin/rbash -p "" kiosk # no need for -r, we need $HOME

# FIXME: this relates to _web_ kiosk
mkdir ~kiosk/.xsession.d
echo firefox > ~kiosk/.xsession.d/firefox
chmod +x ~kiosk/.xsession.d/firefox
# /FIXME

cat >> /etc/sysconfig/autologin << EOF
AUTOLOGIN=yes 
USER=kiosk
EOF 

%files

%changelog
* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- yes, we add pseudo real user not pseudo system user. :)

* Thu Jul 09 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
