# RPM Spec for git-crypt 
git-crypt spec file created for **Fedora** and **CentOS** following the Fedora [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelinesa).

Tested on:
- Fedora 21
- Fedora 22
- CentOS 6
- CentOS 7

## Let's build an RPM
> yum install @development-tools  
> yum install fedora-packager  
> yum install rpmdevtools  
> rpmdev-setuptree  
> wget -P ~/rpmbuild/SOURCES/ https://www.agwa.name/projects/git-crypt/downloads/git-crypt-0.5.0.tar.gz  
> git clone https://github.com/Charg/git-crypt-rpm ~/rpmbuild/SPECS/  
> cd !$  
> rpmbuild -ba git-crypt-spec  

You should now see your git-crypt RPM sitting in `~/rpmbuild/RPMS/x86_64`.
