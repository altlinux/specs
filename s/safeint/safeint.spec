%define _unpackaged_files_terminate_build 1

Name: safeint
Version: 3.0.28a.0.3.git1c94d38
Release: alt1

Summary: dcleblanc's class library for C++ that manages integer overflows

License: MIT
Group: Development/C++
URL: https://github.com/dcleblanc/SafeInt

Source: %name-%version-%release.tar

BuildArch: noarch

%package -n libsafeint-cpp-devel
Summary: dcleblanc's class library for C++ that manages integer overflows
Group: Development/C++
BuildArch: noarch
Requires: %name = %EVR

%package -n libsafeint-c-devel
Summary: dcleblanc's C header-only libraries to manage integer overflows
Group: Development/C
BuildArch: noarch
Requires: %name = %EVR

%description
SafeInt is a class library for C++ that manages integer overflows.

SafeInt is an integer overflow library that was originally created in Microsoft
Office in 2003, and later was made pseudo-open-source on CodePlex using the
MS-PL license. After CodePlex was deprecated, the project was moved to GitHub.
After moving the code to GitHub, the license was changed to the MIT license.

The author is David LeBlanc (dcl@dleblanc.net), portions of the test harness
have come from other contributors. Code written while employed by Microsoft is
copyright Microsoft, code written by the author after leaving Microsoft is
copyright David LeBlanc. Code written by other contributors may have copyright
to that author or their organization.

%description -n libsafeint-c-devel
SafeInt is a class library for C++ that manages integer overflows.

SafeInt is an integer overflow library that was originally created in Microsoft
Office in 2003, and later was made pseudo-open-source on CodePlex using the
MS-PL license. After CodePlex was deprecated, the project was moved to GitHub.
After moving the code to GitHub, the license was changed to the MIT license.

The author is David LeBlanc (dcl@dleblanc.net), portions of the test harness
have come from other contributors. Code written while employed by Microsoft is
copyright Microsoft, code written by the author after leaving Microsoft is
copyright David LeBlanc. Code written by other contributors may have copyright
to that author or their organization.

This package contains the C header based on the same code, safe_math.h.

%description -n libsafeint-cpp-devel
SafeInt is a class library for C++ that manages integer overflows.

SafeInt is an integer overflow library that was originally created in Microsoft
Office in 2003, and later was made pseudo-open-source on CodePlex using the
MS-PL license. After CodePlex was deprecated, the project was moved to GitHub.
After moving the code to GitHub, the license was changed to the MIT license.

The author is David LeBlanc (dcl@dleblanc.net), portions of the test harness
have come from other contributors. Code written while employed by Microsoft is
copyright Microsoft, code written by the author after leaving Microsoft is
copyright David LeBlanc. Code written by other contributors may have copyright
to that author or their organization.

This package contains the SafeInt.hpp C++ header.

%prep
%setup -n %name-%version-%release

%install
install -Dm644 SafeInt.hpp -t %buildroot%_includedir/safeint/
install -Dm644 safe_math.h -t %buildroot%_includedir/safeint/
install -Dm644 safe_math_impl.h -t %buildroot%_includedir/safeint/

%files
%doc helpfile.md

%files -n libsafeint-c-devel
%_includedir/safeint/*.h

%files -n libsafeint-cpp-devel
%_includedir/safeint/*.hpp

%changelog
* Fri Jul 25 2025 Arseny Maslennikov <arseny@altlinux.org> 3.0.28a.0.3.git1c94d38-alt1
- Initial build for ALT Sisyphus.
