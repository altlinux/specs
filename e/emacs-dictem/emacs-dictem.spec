Version: 0.0.2
Release: alt1
Name: emacs-dictem
License: GPL
Group: Editors
Url: http://sf.net/projects/dict
Summary: Dictionary (RFC 2229) client for Emacs
Summary(ru_RU.CP1251):  лиент dictionary (RFC 2229) дл€ Emacs
Summary(be_BY.CP1251):  лiент dictionary (RFC 2229) да Emacs'а
Requires: emacs-common dict

Source: dictem-%version.tar.gz

BuildArch: noarch

BuildRequires: emacs21-common

%description
Dictionary (RFC 2229) client for Emacs

%description -l ru_RU.CP1251
 лиент dictionary (RFC 2229) дл€ Emacs'а

%description -l be_BY.CP1251
 лiент dictionary (RFC 2229) да Emacs'а


%prep
%setup -q -n dictem-%version

%build
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%doc README ChangeLog AUTHORS COPYING
%_emacslispdir/*.elc
%_emacslispdir/*.el

%changelog
* Wed Dec 01 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.0.2-alt1
- New version

* Wed Jul 07 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.0.1-alt1
- First build for ALT project

