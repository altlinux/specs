%define        gemname secure_headers

Name:          gem-secure-headers
Version:       6.3.2
Release:       alt1
Summary:       Manages application of security headers with many safe defaults
License:       Apache Public License 2.0
Group:         Development/Ruby
Url:           https://github.com/twitter/secureheaders
Vcs:           https://github.com/twitter/secureheaders.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names secure_headers,secure-headers
Obsoletes:     ruby-secure-headers < %EVR
Obsoletes:     ruby-securer-headers < %EVR
Provides:      ruby-secure-headers = %EVR
Provides:      ruby-securer-headers = %EVR
Provides:      gem(secure_headers) = 6.3.2


%description
main branch represents 6.x line. See the upgrading to 4.x doc, upgrading to 5.x
doc, or upgrading to 6.x doc for instructions on how to upgrade. Bug fixes
should go in the 5.x branch for now.

The gem will automatically apply several headers that are related to security.
This includes:

* Content Security Policy (CSP) - Helps detect/prevent XSS, mixed-content, and
  other classes of attack. CSP 2 Specification
 * https://csp.withgoogle.com
 * https://csp.withgoogle.com/docs/strict-csp.html
 * https://csp-evaluator.withgoogle.com
* HTTP Strict Transport Security (HSTS) - Ensures the browser never visits the
  http version of a website. Protects from SSLStrip/Firesheep attacks. HSTS
  Specification
* X-Frame-Options (XFO) - Prevents your content from being framed and
  potentially clickjacked. X-Frame-Options Specification
* X-XSS-Protection - Cross site scripting heuristic filter for IE/Chrome
* X-Content-Type-Options - Prevent content type sniffing
* X-Download-Options - Prevent file downloads opening
* X-Permitted-Cross-Domain-Policies - Restrict Adobe Flash Player's access to
  data
* Referrer-Policy - Referrer Policy draft
* Expect-CT - Only use certificates that are present in the certificate
  transparency logs. Expect-CT draft specification.
* Clear-Site-Data - Clearing browser data for origin. Clear-Site-Data
  specification.

It can also mark all http cookies with the Secure, HttpOnly and SameSite
attributes. This is on default but can be turned off by using
'config.cookies = SecureHeaders::OPT_OUT'.

secure_headers is a library with a global config, per request overrides, and
rack middleware that enables you customize your application settings.


%package       -n gem-secure-headers-doc
Version:       6.3.2
Release:       alt1
Summary:       Manages application of security headers with many safe defaults documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета secure_headers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(secure_headers) = 6.3.2

%description   -n gem-secure-headers-doc
Manages application of security headers with many safe defaults documentation
files.

main branch represents 6.x line. See the upgrading to 4.x doc, upgrading to 5.x
doc, or upgrading to 6.x doc for instructions on how to upgrade. Bug fixes
should go in the 5.x branch for now.

The gem will automatically apply several headers that are related to security.
This includes:

* Content Security Policy (CSP) - Helps detect/prevent XSS, mixed-content, and
  other classes of attack. CSP 2 Specification
 * https://csp.withgoogle.com
 * https://csp.withgoogle.com/docs/strict-csp.html
 * https://csp-evaluator.withgoogle.com
* HTTP Strict Transport Security (HSTS) - Ensures the browser never visits the
  http version of a website. Protects from SSLStrip/Firesheep attacks. HSTS
  Specification
* X-Frame-Options (XFO) - Prevents your content from being framed and
  potentially clickjacked. X-Frame-Options Specification
* X-XSS-Protection - Cross site scripting heuristic filter for IE/Chrome
* X-Content-Type-Options - Prevent content type sniffing
* X-Download-Options - Prevent file downloads opening
* X-Permitted-Cross-Domain-Policies - Restrict Adobe Flash Player's access to
  data
* Referrer-Policy - Referrer Policy draft
* Expect-CT - Only use certificates that are present in the certificate
  transparency logs. Expect-CT draft specification.
* Clear-Site-Data - Clearing browser data for origin. Clear-Site-Data
  specification.

It can also mark all http cookies with the Secure, HttpOnly and SameSite
attributes. This is on default but can be turned off by using
'config.cookies = SecureHeaders::OPT_OUT'.

secure_headers is a library with a global config, per request overrides, and
rack middleware that enables you customize your application settings.


%description   -n gem-secure-headers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета secure_headers.


%package       -n gem-secure-headers-devel
Version:       6.3.2
Release:       alt1
Summary:       Manages application of security headers with many safe defaults development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета secure_headers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(secure_headers) = 6.3.2
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-secure-headers-devel
Manages application of security headers with many safe defaults development
package.

main branch represents 6.x line. See the upgrading to 4.x doc, upgrading to 5.x
doc, or upgrading to 6.x doc for instructions on how to upgrade. Bug fixes
should go in the 5.x branch for now.

The gem will automatically apply several headers that are related to security.
This includes:

* Content Security Policy (CSP) - Helps detect/prevent XSS, mixed-content, and
  other classes of attack. CSP 2 Specification
 * https://csp.withgoogle.com
 * https://csp.withgoogle.com/docs/strict-csp.html
 * https://csp-evaluator.withgoogle.com
* HTTP Strict Transport Security (HSTS) - Ensures the browser never visits the
  http version of a website. Protects from SSLStrip/Firesheep attacks. HSTS
  Specification
* X-Frame-Options (XFO) - Prevents your content from being framed and
  potentially clickjacked. X-Frame-Options Specification
* X-XSS-Protection - Cross site scripting heuristic filter for IE/Chrome
* X-Content-Type-Options - Prevent content type sniffing
* X-Download-Options - Prevent file downloads opening
* X-Permitted-Cross-Domain-Policies - Restrict Adobe Flash Player's access to
  data
* Referrer-Policy - Referrer Policy draft
* Expect-CT - Only use certificates that are present in the certificate
  transparency logs. Expect-CT draft specification.
* Clear-Site-Data - Clearing browser data for origin. Clear-Site-Data
  specification.

It can also mark all http cookies with the Secure, HttpOnly and SameSite
attributes. This is on default but can be turned off by using
'config.cookies = SecureHeaders::OPT_OUT'.

secure_headers is a library with a global config, per request overrides, and
rack middleware that enables you customize your application settings.

%description   -n gem-secure-headers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета secure_headers.


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

%files         -n gem-secure-headers-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-secure-headers-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 6.3.2-alt1
- ^ 6.3.0 -> 6.3.2

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1.1
- ! spec obsoletes/provides

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- updated (^) 6.1.1 -> 6.3.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- updated (^) 6.0.0 -> 6.1.1
- used (>) Ruby Policy 2.0

* Wed Sep 26 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt2
- updated (^) 5.0.5 -> 6.0.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.0.5-alt1
- downgraded (v) 6.0.0 -> 5.0.5 for foreman.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- Initial build for Sisyphus
