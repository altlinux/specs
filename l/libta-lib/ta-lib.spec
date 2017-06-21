%define sourcename ta-lib
Name: libta-lib
Version: 0.4.0
Release: alt1
Summary: TA LIB

Group: Development/Other
License: BSD
Url: http://ta-lib.org/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %sourcename-%version.tar
BuildRequires:	gcc-c++

%description
TA-Lib is widely used by trading software developers requiring to perform technical analysis of financial market data.
Includes 200 indicators such as ADX, MACD, RSI, Stochastic, Bollinger Bands, etc.
Candlestick pattern recognition
Open-source API for C/C++, Java, Perl, Python and 100% Managed .NET

%prep
%setup -n %sourcename-%version

%build
#./autogen.sh
#libtoolize -f
%configure LDFLAGS="-lm"
%make_build

%install
%makeinstall_std

%files
%doc HISTORY.TXT CHANGELOG.TXT
%_bindir/ta-lib-config
%_libdir/libta_lib*
%_includedir/ta-lib

%changelog
* Wed Jun 21 2017 Konstantin Artyushkin <akv@altlinux.org> 0.4.0-alt1
- initial build



