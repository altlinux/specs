Name: python-module-irclib
Version: 0.4.8
Release: alt1

%setup_python_module irclib

Summary: A set of Python modules for IRC support.
License: LGPL
Group: Development/Python
Url: http://python-irclib.sourceforge.net

Packager: Alexey Gladkov <legion@altlinux.org>

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
This library is intended to encapsulate the IRC protocol at a quite
low level.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%prep
%setup

%build
%__python setup.py build

%install
%__python setup.py install \
    --root=%buildroot \
    --optimize=2 \
    --record=INSTALLED_FILES

# we have rpm for that, btw
sed -i '/egg-info/d' INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README ChangeLog COPYING irccat irccat2 servermap testbot.py dccsend dccreceive

%changelog
* Sat Dec 24 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.8-alt1
- initial build for Sisyphus

