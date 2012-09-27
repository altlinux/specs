Name:		python-module-netaddr
Version:	0.7.5
Release:	alt1
Summary:	A pure Python network address representation and manipulation library

Group:		Development/Python
License:	BSD
URL:		http://github.com/drkjam/netaddr
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel >= 2.4

Patch0:		%{name}-fixed-github-issue-2.patch


%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets
- MAC addresses, OUI and IAB identifiers, IEEE EUI-64 identifiers
- arbitrary (non-aligned) IP address ranges and IP address sets
- various non-CIDR IP range formats such as nmap and glob-style formats

Included are routines for :-

- generating, sorting and summarizing IP addresses and networks
- performing easy conversions between address notations and formats
- detecting, parsing and formatting network address representations
- performing set-based operations on groups of IP addresses and subnets
- working with arbitrary IP address ranges and formats
- accessing OUI and IAB organisational information published by IEEE
- accessing IP address and block information published by IANA

For details on the latest updates and changes, see :-

    http://github.com/drkjam/netaddr/blob/rel-0.7.x/CHANGELOG

API documentation for the latest release is available here :-

    http://packages.python.org/netaddr/

%prep
%setup -q
%patch0 -p1 -b .invalid_ip_network

# Make rpmlint happy, get rid of DOS line endings
%{__sed} -i 's/\r//' netaddr/*.py
%{__sed} -i 's/\r//' netaddr/ip/*.py
%{__sed} -i 's/\r//' netaddr/eui/*.idx

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs %{__perl} -ni -e 'print unless /usr\/bin\/python|env\s+python/'

# Make rpmlint happy, fix permissions on documentation files
chmod 0644 README AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE PKG-INFO

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} netaddr/tests/__init__.py

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE PKG-INFO
%doc README docs/api/
%{python_sitelibdir}/*
%{_bindir}/netaddr

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.5-alt1
- Initial release for Sisyphus (based on Fedora)
