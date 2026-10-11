%define node_module mocha

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-mocha
Version: 12.0.3
Release: alt1

Summary: simple, flexible, fun javascript test framework for node.js & the browser

License: MIT License
Group: Development/Other
Url: https://github.com/mochajs/mocha

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mochajs/mocha/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 20.19
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
# due to AutoProv: no
Provides: npm(mocha) = %version
Requires: node

%description
Mocha is a feature-rich JavaScript test framework running on Node.js
and in the browser, making asynchronous testing simple and fun.
Mocha tests run serially, allowing for flexible and accurate reporting,
while mapping uncaught exceptions to the correct test cases.

%prep
%setup -a 1

%build
#pm prune --production

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/mocha.js %buildroot%_bindir/mocha
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/docs/

%check
%buildroot%_bindir/mocha --version

%files
%doc LICENSE README.md
%_bindir/mocha
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 12.0.3-alt1
- new version 12.0.3
- require node >= 20.19 (upstream engines requirement)
- apply npm audit fix to production dependencies via predownloaded-postinstall-hook
- security fixes:
  + CVE-2024-21538, GHSA-3xgq-45jj-v275: cross-spawn ReDoS (no longer shipped).
  + CVE-2025-5889, GHSA-v6h2-p8h4-qcjw: brace-expansion ReDoS.
  + CVE-2026-13149, GHSA-3jxr-9vmj-r5cp: brace-expansion DoS via exponential expansion of non-expanding {} groups.
  + CVE-2026-14257, GHSA-mh99-v99m-4gvg: brace-expansion DoS via unbounded expansion length.
  + CVE-2026-33750, GHSA-f886-m6hf-6m8v: brace-expansion hang on zero-step sequence.
  + CVE-2026-69152, GHSA-rgw5-rvv9-x895: brace-expansion DoS via unbounded intermediate arrays.
  + CVE-2026-102276, GHSA-6j4f-fj2g-mc7p: brace-expansion stack exhaustion in parseCommaParts.
  + CVE-2026-102277, GHSA-q2hr-2g5m-vwhr: brace-expansion quadratic-time expansion of {a},b} rewrite.
  + CVE-2026-102278, GHSA-qhr7-859c-m2p7: brace-expansion stack exhaustion on nested brace groups.
  + CVE-2026-24001, GHSA-73rr-hh4g-fpgx: jsdiff DoS in parsePatch and applyPatch.
  + CVE-2025-64756, GHSA-5j98-mcp5-4vw2: glob CLI command injection via -c/--cmd.
  + CVE-2025-64718, GHSA-mh29-5h37-fv8m: js-yaml prototype pollution in merge (<<).
  + CVE-2026-53550, GHSA-h67p-54hq-rp68: js-yaml quadratic DoS in merge key handling via repeated aliases.
  + CVE-2026-59869, GHSA-52cp-r559-cp3m: js-yaml quadratic CPU consumption via merge-key chains.
  + CVE-2026-84375, GHSA-2883-xcg3-v3hh: js-yaml maxTotalMergeKeys does not limit CPU for empty merge sources.
  + GHSA-5p4m-2wfm-xmqj: js-yaml quadratic CPU consumption in !!omap resolution.
  + CVE-2026-26996, GHSA-3ppc-4f35-3m26: minimatch ReDoS via repeated wildcards.
  + CVE-2026-27903, GHSA-7r86-cg39-jmmj: minimatch ReDoS via multiple non-adjacent GLOBSTAR segments.
  + CVE-2026-27904, GHSA-23c5-xmqv-rm74: minimatch ReDoS via nested *() extglobs.
  + CVE-2026-34043, GHSA-qj8w-gfj5-8c6v: serialize-javascript CPU exhaustion via array-like objects.
  + GHSA-5c6j-r48x-rmvq: serialize-javascript RCE via RegExp.flags and Date.prototype.toISOString().

* Tue Sep 01 2026 Vitaly Lipatov <lav@altlinux.ru> 11.7.7-alt2
- Fixed /usr/bin/mocha symlink (ALT bug 60309).

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 11.7.7-alt1
- new version 11.7.7

* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 11.7.5-alt1
- new version 11.7.5

* Sun Jan 26 2025 Vitaly Lipatov <lav@altlinux.ru> 11.1.0-alt1
- new version 11.1.0 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 9.1.3-alt1
- new version 9.1.3 (with rpmrb script)

* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt2
- NMU: added provides: npm(mocha) for autoimports

* Wed Mar 04 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt1
- new version 7.1.0 (with rpmrb script)

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- initial build for ALT Sisyphus
