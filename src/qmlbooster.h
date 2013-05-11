#ifndef QMLBOOSTER_H
#define QMLBOOSTER_H

#include "eventhandler.h"
#include "booster.h"

class QMLBooster : public Booster
{
public:
    virtual const std::string &boosterType() const;
    virtual bool preload();

protected:
    virtual bool receiveDataFromInvoker(int socketFd);
    virtual void preinit();

private:
    static const std::string m_boosterType;
};

#endif
