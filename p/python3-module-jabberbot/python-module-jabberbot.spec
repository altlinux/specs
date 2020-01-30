%define _unpackaged_files_terminate_build 1
%define oname jabberbot

Name: python3-module-%oname
Version: 0.16
Release: alt2

Summary: A simple jabber/xmpp bot framework
License: GPLv3+
Group: Development/Python3
Url: http://thpinfo.com/2007/python-jabberbot

BuildArch: noarch

Source0: https://pypi.python.org/packages/82/e7/36cc193d99498cc42ac8909e2b028202ac7ac6ec8c615f61d5331dbdbba4/jabberbot-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-xmpp python-tools-2to3

Requires: python3-module-xmpp


%description
Programming your own Jabber bot can be fun and helpful. This is
python-jabberbot, a Jabber bot framework for Python that enables you to
easily write simple Jabber bots. You can use your Jabber bots to provide
information about your running systems, to make your website interact
with your visitors or notify you about updates or changes you monitor
with your Python scripts.

%prep
%setup -q -n jabberbot-%{version}

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc examples README AUTHORS
%python3_sitelibdir/*.py*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/__pycache__/%oname.*


%changelog
* Thu Jan 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.16-alt2
- Porting on Python3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated PyPI update

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt3.1
- Rebuild with Python-2.7

* Wed Apr 21 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt3
- jabberbot.py: strip resource name from jid when getting subscribtion
  for avoid bot crash when resource name contains non-ascii characters.
- Update buildreqs.

* Tue Apr 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt2
- Package documentation.

* Tue Apr 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt1
- Initial build for Sisyphus.

