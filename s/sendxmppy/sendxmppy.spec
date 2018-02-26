Name: sendxmppy
Version: 0.5.1
Release: alt1.1

Summary: XMPP message sender from CLI

License: BSD
Group: Networking/Instant messaging
Url: http://git.altlinux.org/people/zver/packages/sendxmppy.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel

%description
XMPP message sender from CLI

%prep
%setup

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 26 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1
- 0.5.1:
  + Change config file picking behavior. Don't fall out if no HOME env
    var are present.

* Wed Oct 20 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.0-alt1
- 0.5.0:
  + Use argparse module for arguments parsing.
  + Use xmpp (xmpppy) module for sending messages. As an effect of this,
    sendxmppy supports SRV records now.
  + Incompatible changes: options -u/--username and -j/--jserver
    replaced with -j/--jid
- Update BuildRequires, remove manually-added Requires

* Mon Feb 01 2010 Denis Klimov <zver@altlinux.org> 0.4.2-alt1
- new version

* Mon Jan 25 2010 Denis Klimov <zver@altlinux.org> 0.4.1-alt1
- new version

* Wed Jan 06 2010 Denis Klimov <zver@altlinux.org> 0.4-alt1
- new version

* Mon Jan 04 2010 Denis Klimov <zver@altlinux.org> 0.3-alt2
- add require to python-module-jabberpy (Closes: #22678)

* Sun Dec 13 2009 Denis Klimov <zver@altlinux.org> 0.3-alt1
- new version

* Sat Nov 28 2009 Denis Klimov <zver@altlinux.org> 0.2-alt2
- add build require to python-dev

* Wed Nov 25 2009 Denis Klimov <zver@altlinux.org> 0.2-alt1
- new version

* Wed Nov 25 2009 Denis Klimov <zver@altlinux.org> 0.1-alt1
- Initial build for ALT Linux

