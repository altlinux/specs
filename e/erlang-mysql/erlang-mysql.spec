Name: erlang-mysql
Version: 0.0
Release: alt1.svn1031
Packager: Anton Gorlov <stalker@altlinux.ru>

Summary: MySQL frontend for Erlang
License: BSD license
Group: Development/Erlang
URL: https://support.process-one.net/doc/display/CONTRIBS/Yxa

Source: %name-%version.tar.gz

BuildArch: noarch

Requires: erlang-otp-common
BuildRequires: erlang-otp rpm-build-erlang
#{?_with_native:BuildRequires: /proc}

%description
This MySQL driver for Erlang is based on the Yxa driver obtained 
from Process One (at https://support.process-one.net/doc/display/CONTRIBS/Yxa)
It includes several new features such as prepared statements, transactions, binary queries,
type-converted query results, more efficient logging and a new connection pooling mechanism.

%prep
%setup -q

%build
mkdir -p %name-%version/ebin

sed -i 's/ebin/%name-%version\/ebin/g' Emakefile
./build.sh

%install
#%make_install PREFIX=%buildroot/%_usr install

mkdir -p %buildroot/%_otplibdir
cp -r %name-%version %buildroot/%_otplibdir

%files
%dir %_otplibdir/%name-%version
%_otplibdir/%name-%version/

%changelog
* Tue Mar 22 2011 Anton Gorlov <stalker@altlinux.ru> 0.0-alt1.svn1031
- fix build req

* Tue Dec 01 2009 Anton Gorlov <stalker@altlinux.ru> 0.0-alt0.svn1031
- Initial build for ALTLinux 


