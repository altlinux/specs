%define        gemname time

Name:          gem-time
Version:       0.2.0
Release:       alt1
Summary:       Extends the Time class with methods for parsing and conversion
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/time
Vcs:           https://github.com/ruby/time.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(date) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(date) >= 0
Provides:      gem(time) = 0.2.0


%description
When 'time' is required, Time is extended with additional methods for parsing
and converting Times.

This library extends the Time class with the following conversions between date
strings and Time objects:
* date-time defined by {RFC 2822}[http://www.ietf.org/rfc/rfc2822.txt]
* HTTP-date defined by {RFC 2616}[http://www.ietf.org/rfc/rfc2616.txt]
* dateTime defined by XML Schema Part 2: Datatypes ({ISO 8601}[http://www.iso.org/iso/date_and_time_format])
* various formats handled by Date._parse
* custom formats handled by Date._strptime


%package       -n gem-time-doc
Version:       0.2.0
Release:       alt1
Summary:       Extends the Time class with methods for parsing and conversion documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета time
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(time) = 0.2.0

%description   -n gem-time-doc
Extends the Time class with methods for parsing and conversion documentation
files.

When 'time' is required, Time is extended with additional methods for parsing
and converting Times.

This library extends the Time class with the following conversions between date
strings and Time objects:
* date-time defined by {RFC 2822}[http://www.ietf.org/rfc/rfc2822.txt]
* HTTP-date defined by {RFC 2616}[http://www.ietf.org/rfc/rfc2616.txt]
* dateTime defined by XML Schema Part 2: Datatypes ({ISO 8601}[http://www.iso.org/iso/date_and_time_format])
* various formats handled by Date._parse
* custom formats handled by Date._strptime

%description   -n gem-time-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета time.


%package       -n gem-time-devel
Version:       0.2.0
Release:       alt1
Summary:       Extends the Time class with methods for parsing and conversion development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета time
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(time) = 0.2.0

%description   -n gem-time-devel
Extends the Time class with methods for parsing and conversion development
package.

When 'time' is required, Time is extended with additional methods for parsing
and converting Times.

This library extends the Time class with the following conversions between date
strings and Time objects:
* date-time defined by {RFC 2822}[http://www.ietf.org/rfc/rfc2822.txt]
* HTTP-date defined by {RFC 2616}[http://www.ietf.org/rfc/rfc2616.txt]
* dateTime defined by XML Schema Part 2: Datatypes ({ISO 8601}[http://www.iso.org/iso/date_and_time_format])
* various formats handled by Date._parse
* custom formats handled by Date._strptime

%description   -n gem-time-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета time.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-time-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-time-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
