Name: kotlin
Version: 1.3.72
Release: alt1

Summary: Kotlin Programming Language
License: Apache-2.0 and BSD and MIT and NPL-1.1 and BSL-1.0
Group: Development/Java

Url: http://www.kotlin-lang.org/
Source: http://github.com/JetBrains/kotlin/releases/download/v%version/kotlin-compiler-%version.zip

BuildRequires: unzip
Requires: java

BuildArch: noarch
AutoReqProv: no

%description
Kotlin is a general purpose statically typed cross-platform programming
language designed around JVM. It was developed as an alternative
to Java and is officially supported for Android application development.

This package contains jars prebuilt by the language creator, JetBrains
(compiler only, IDE like IntelliJ IDEA not included).

%prep
%setup -n kotlinc

%build

%install
mkdir -p %buildroot{%_datadir/%name/bin,%_bindir}
cp -alt %buildroot%_datadir/%name -- lib
for i in kotlin kotlin-dce-js kotlinc kotlinc-js kotlinc-jvm kapt; do
	cp -at %buildroot%_datadir/%name/bin -- bin/$i
	ln -sr %buildroot{%_datadir/%name/bin,%_bindir}/$i 
done

%files
%doc license
%_bindir/*
%_datadir/%name/

%changelog
* Thu Jul 16 2020 Michael Shigorin <mike@altlinux.org> 1.3.72-alt1
- BuildArch: noarch

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 1.3.72-alt1
- initial release

