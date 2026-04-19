%global _unpackaged_files_terminate_build 1
# git rev-parse --short v%version
%global commit_hash 7f55800

Name: gemini-cli
Version: 0.38.1
Release: alt1
Summary: AI agent that brings the power of Gemini directly into your terminal
License: Apache-2.0
Group: Development/Tools
Url: https://geminicli.com
VCS: https://github.com/google-gemini/gemini-cli

Source: %name-%version.tar
Source1: node_modules.tar
Source2: node_modules_cli.tar
Source3: node_modules_core.tar
Source4: node_modules_a2a.tar
Source5: gemini.sh

BuildArch: noarch

BuildRequires: esbuild
BuildRequires: npm

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini
directly into your terminal. It provides lightweight access to Gemini,
giving you the most direct path from your prompt to our model.

%prep
%setup -a 1 -a 2 -a 3 -a 4
mkdir -p packages/{core,cli}/src/generated
tee packages/{core,cli}/src/generated/git-commit.{js,ts} <<EOF
export const GIT_COMMIT_INFO = '%commit_hash';
export const CLI_VERSION = '%version';
EOF

mkdir -p packages/devtools/dist/src
tee packages/devtools/dist/src/index.d.ts <<'EOF'
export interface NetworkLog { id: string; url?: string; }
export interface ConsoleLogPayload { message?: string; }
export interface InspectorConsoleLog extends ConsoleLogPayload { id: string; timestamp: number; }
export interface SessionInfo { sessionId: string; }
export class DevTools {
  private static instance: DevTools | undefined;
  private constructor();
  static getInstance(): DevTools;
  start(): Promise<string>;
  stop(): Promise<void>;
  getPort(): number;
}
EOF

# use system esbuild
ln -sv %_bindir/esbuild .
sed -i "s/0.25.6/$(rpm -q --qf '%{VERSION}' esbuild)/g" node_modules/esbuild/lib/main.js

%build
export ESBUILD_BINARY_PATH=./esbuild
cd packages/cli
npm run build
cd -
node esbuild.config.js

%install
mkdir -p %buildroot%_bindir %buildroot%_libexecdir/%name/policies
cp bundle/* %buildroot%_libexecdir/%name
cp packages/core/src/policy/policies/*.toml %buildroot%_libexecdir/%name/policies
install -m 0755 %SOURCE5 %buildroot%_bindir/gemini
rm -vf %buildroot%_libexecdir/%name/getMachineId-{win,darwin,bsd}-*.js

%files
%_bindir/gemini
%_libexecdir/%name
%doc LICENSE

%changelog
* Sun Apr 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.38.1-alt1
- Updated to version 0.38.1.

* Thu Mar 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.0-alt1
- Updated to version 0.34.0.

* Sat Feb 28 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.30.1-alt1
- Updated to version 0.30.1.

* Thu Feb 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.29.2-alt1
- Updated to version 0.29.2.

* Wed Feb 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.29.0-alt1
- Updated to version 0.29.0.

* Sat Feb 07 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.27.3-alt1
- Updated to version 0.27.3.

* Fri Feb 06 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.27.2-alt1
- Updated to version 0.27.2.

* Sun Feb 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.26.0-alt1
- Updated to version 0.26.0.

* Sat Jan 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.25.1-alt1
- Updated to version 0.25.1.

* Tue Jan 20 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.24.5-alt1
- Updated to version 0.24.5.

* Sun Jan 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.24.0-alt1
- Updated to version 0.24.0.

* Sun Dec 28 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.22.3-alt1
- Updated to version 0.22.3.

* Mon Dec 15 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.20.2-alt1
- Updated to version 0.20.2.

* Wed Dec 03 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.19.1-alt1
- Updated to version 0.19.1.

* Sun Nov 30 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.18.3-alt1
- Initial build for ALT.
