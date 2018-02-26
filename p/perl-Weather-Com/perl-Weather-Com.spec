## SPEC file for Perl module Weather::Com

%define version    0.5.5
%define release    alt1

Name: perl-Weather-Com
Version: %version
Release: alt1.1

Summary: Perl module for accessing weather information
Summary(ru_RU.UTF-8): модуль Perl для получения информации о погоде

License: %perl_license
Group: Development/Perl

%define real_name Weather-Com
URL: http://search.cpan.org/~schnueck/Weather-Com/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses
BuildRequires: perl-Time-Format, perl-Time-Format_XS, perl-Test-MockObject
BuildRequires: perl-Locale-Maketext, perl-libwww, perl-XML-Simple

%description
Weather::Com  is a Perl module enabling the programmer to access weather
information as provided by weather.com's XMLOAP interface.

By XMLOAP API  weather.com provides current conditions and up to 10 days
of forecast containing most information one could need, e.g. the time of
sunrise  and sunset,  the longitude  and latitude of  the location, data 
precompiled either in the US system or in the metric system, etc. 

For using the weather.com's service a free registration is needed:
http://www.weather.com/services/xmloap.html. You will  be send  an email
containing your 'partner id', a license key and a link where to download
the SDK with implementation guides, weather icons in several sizes, 'The
Weather Channel' logos, etc..

%description -l ru_RU.UTF-8
Модуль Perl Weather::Com позволяет программисту работать с информацией 
о погоде, предоставляемой через интерфейс XMLOAP сайта weather.com.

Через API XMLOAP  можно  получить текущую сводку погоды и  прогнозы на 
ближайшие 10 дней. Помимо сведений о погоде предоставляется информация 
о времени восхода и заката солнца, широта и долгота места, пр.

Для использования сервиса  weather.com  требуется  пройти бесплатную 
регистрацию на  http://www.weather.com/services/xmloap.html. В ответ 
будет получено  письмо с 'partner id',  ключом регистрации и ссылкой 
на SDK с описанием протокола, примерами использования, пиктограммами
для отображения данных на веб-страницах, и т.п.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README BUGS TODO
%doc samples/*
%exclude /.perl.req
%dir %perl_vendor_privlib/Weather
%perl_vendor_privlib/Weather/Com*


%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.5-alt1
- New version 0.5.5

* Wed May 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt2
- Fix for changed weather.com API (rt.cpan.org #35681)

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt1
- New version 0.5.3

* Wed Aug 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.2-alt1
- New version 0.5.2
  - Fixed bug (rt.cpan.org #26126): Timeout did not work due to typo 
  - Fixed bug (rt.cpan.org #25154): (test within OOInterface.t failed)
  - Fixed bug (rt.cpan.org #25151): Installing Weather-Com install 0.1
  - Fixed bug: test for network connection failed due to more New Yorks... 
		
* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.1-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.1-alt0
- Initial build
