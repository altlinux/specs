%define _unpackaged_files_terminate_build 1
%define  pkgname sanitize

Name: gem-%pkgname
Version: 7.0.0
Release: alt1

Summary: Ruby HTML and CSS sanitizer 
License: MIT
Group: Development/Ruby
Url: https://github.com/rgrove/sanitize/
VCS: https://github.com/rgrove/sanitize/ 
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
Sanitize is an allowlist-based HTML and CSS sanitizer. It removes 
all HTML and/or CSS from a string except the elements, attributes,
and properties you choose to allow.

Using a simple configuration syntax, you can tell Sanitize to allow
certain HTML elements, certain attributes within those elements, 
and even certain URL protocols within attributes that contain URLs. 
You can also allow specific CSS properties, @ rules, and URL protocols
in elements or attributes containing CSS. Any HTML or CSS that you 
don't explicitly allow will be removed.

Sanitize is based on the Nokogiri HTML5 parser, which parses HTML the
same way modern browsers do, and Crass, which parses CSS the same way
modern browsers do. As long as your allowlist config only allows safe
markup and CSS, even the most malformed or malicious input will be 
transformed into safe output.


%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Aleksandr Dovydenkov <asd@altlinux.org> 7.0.0-alt1
- Initial build for ALT Linux.
