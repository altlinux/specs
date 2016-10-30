Name: json-cpp
Version: 2.0.6
Release: alt0.1

Summary: JSON for Modern C++ (c++11) ("single header file")

License: GPL
Group: Development/C++
Url: https://github.com/nlohmann/json

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Git: https://github.com/nlohmann/json
Source: %name-%version.tar

#BuildRequires:

%description
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax. 
- Trivial integration.
- Serious testing

%prep
%setup 

%build

%install
mkdir -p %buildroot%_includedir
mv -f src/json.hpp %buildroot%_includedir

%files
%_includedir/*.hpp

%changelog
* Sun Oct 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.6-alt0.1
- initial commit 
