%define        gemname ruby-msg

Name:          gem-ruby-msg
Version:       1.5.2
Release:       alt2.1
Summary:       A library for reading and converting Outlook msg and pst files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aquasync/ruby-msg
Vcs:           https://github.com/aquasync/ruby-msg.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ruby-ole) >= 1.2.8
BuildRequires: gem(vpim) >= 0.360

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ruby-ole) >= 1.2.8
Requires:      gem(vpim) >= 0.360
Provides:      gem(ruby-msg) = 1.5.2


%description
A library for reading and converting Outlook msg and pst files (mapi message
stores).

Generally, the goal of the project is to enable the conversion of msg and pst
files into standards based formats, without reliance on outlook, or any
platform dependencies. In fact its currently pure ruby, so it should be easy to
get running.

It is targeted at people who want to migrate their PIM data from outlook,
converting msg and pst files into rfc2822 emails, vCard contacts, iCalendar
appointments etc. However, it also aims to be a fairly complete mapi message
store manipulation library, providing a sane model for (currently read-only)
access to msg and pst files (message stores).


%package       -n mapitool
Version:       1.5.2
Release:       alt2.1
Summary:       A library for reading and converting Outlook msg and pst files executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-msg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-msg) = 1.5.2

%description   -n mapitool
A library for reading and converting Outlook msg and pst files executable(s).

A library for reading and converting Outlook msg and pst files (mapi message
stores).

Generally, the goal of the project is to enable the conversion of msg and pst
files into standards based formats, without reliance on outlook, or any
platform dependencies. In fact its currently pure ruby, so it should be easy to
get running.

It is targeted at people who want to migrate their PIM data from outlook,
converting msg and pst files into rfc2822 emails, vCard contacts, iCalendar
appointments etc. However, it also aims to be a fairly complete mapi message
store manipulation library, providing a sane model for (currently read-only)
access to msg and pst files (message stores).

%description   -n mapitool -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-msg.


%package       -n gem-ruby-msg-doc
Version:       1.5.2
Release:       alt2.1
Summary:       A library for reading and converting Outlook msg and pst files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-msg
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-msg) = 1.5.2

%description   -n gem-ruby-msg-doc
A library for reading and converting Outlook msg and pst files documentation
files.

A library for reading and converting Outlook msg and pst files (mapi message
stores).

Generally, the goal of the project is to enable the conversion of msg and pst
files into standards based formats, without reliance on outlook, or any
platform dependencies. In fact its currently pure ruby, so it should be easy to
get running.

It is targeted at people who want to migrate their PIM data from outlook,
converting msg and pst files into rfc2822 emails, vCard contacts, iCalendar
appointments etc. However, it also aims to be a fairly complete mapi message
store manipulation library, providing a sane model for (currently read-only)
access to msg and pst files (message stores).

%description   -n gem-ruby-msg-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-msg.


%package       -n gem-msg-devel
Version:       1.5.2
Release:       alt2.1
Summary:       A library for reading and converting Outlook msg and pst files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-msg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-msg) = 1.5.2

%description   -n gem-msg-devel
A library for reading and converting Outlook msg and pst files development
package.

A library for reading and converting Outlook msg and pst files (mapi message
stores).

Generally, the goal of the project is to enable the conversion of msg and pst
files into standards based formats, without reliance on outlook, or any
platform dependencies. In fact its currently pure ruby, so it should be easy to
get running.

It is targeted at people who want to migrate their PIM data from outlook,
converting msg and pst files into rfc2822 emails, vCard contacts, iCalendar
appointments etc. However, it also aims to be a fairly complete mapi message
store manipulation library, providing a sane model for (currently read-only)
access to msg and pst files (message stores).

%description   -n gem-msg-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-msg.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n mapitool
%doc README
%_bindir/mapitool

%files         -n gem-ruby-msg-doc
%doc README
%ruby_gemdocdir

%files         -n gem-msg-devel
%doc README


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2.1
- ! spec

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- Use Ruby Policy 2.0

* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus bumped to 1.5.2
